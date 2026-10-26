---
url: https://docs.comfy.org/es/interface/apps/
title: Barra lateral Aplicaciones - Aplicaciones de flujo de trabajo empaquetadas - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:28.714954+00:00
---

# Barra lateral Aplicaciones - Aplicaciones de flujo de trabajo empaquetadas - ComfyUI

> Source: https://docs.comfy.org/es/interface/apps/

## En esta página

Volver arriba

  * Abrir el panel Aplicaciones
  * Estado vacío y Crear
  * Trabajar con aplicaciones
  * Cómo se relacionan Aplicaciones con Flujos de trabajo y Plantillas
  * Páginas relacionadas



Barra lateral izquierda

# Barra lateral Aplicaciones - Aplicaciones de flujo de trabajo empaquetadas

Copiar páginaCopiar página

La pestaña Aplicaciones de la barra lateral lista aplicaciones de flujo de trabajo empaquetadas (.app.json). Para la interfaz lineal, consulta modo aplicación.

Copiar páginaCopiar página

La entrada **Aplicaciones** se registra en la barra lateral izquierda después de Recursos, Biblioteca de nodos, Biblioteca de modelos y Flujos de trabajo. Lista aplicaciones de flujo de trabajo empaquetadas: flujos de trabajo guardados cuyo sufijo de archivo es `.app.json`. El título de la pestaña incluye una insignia **Beta**. Este catálogo de la barra lateral no es lo mismo que el [Modo App](https://docs.comfy.org/es/interface/app-mode). El Modo App es la interfaz de ejecución lineal y simplificada de un flujo de trabajo. La barra lateral Aplicaciones es donde encuentras y abres aplicaciones empaquetadas, creas un flujo de trabajo en blanco para empezar uno nuevo y administras esos archivos `.app.json` de la misma manera en que administras flujos de trabajo normales. ![El panel Aplicaciones con la insignia Beta, el botón Crear y las aplicaciones guardadas en Explorar](https://mintcdn.com/dripart/cWths51SAUr51YVL/images/interface/apps/apps_panel.png?fit=max&auto=format&n=cWths51SAUr51YVL&q=85&s=5c19665329960a9e62c1c8f3ec78f807)

## 

​

Abrir el panel Aplicaciones

Haz clic en el icono **Aplicaciones** de la barra lateral izquierda. El panel reutiliza el mismo diseño que [Flujos de trabajo](https://docs.comfy.org/es/interface/workflows): búsqueda, sección **Abrir** opcional (cuando los flujos de trabajo abiertos están configurados en Barra lateral), **Marcadores** y **Explorar** , pero cada lista se filtra para mostrar solo archivos `.app.json`.

## 

​

Estado vacío y Crear

Cuando aún no hay aplicaciones guardadas, el área Explorar muestra un estado vacío con un mensaje breve y un botón **Crear aplicación**. Cuando la lista de Explorar tiene resultados, también aparece un botón **Crear** en el encabezado del panel. Ambas acciones ejecutan **Nuevo flujo de trabajo en blanco** (`Comfy.NewBlankWorkflow`), que abre un gráfico en blanco que puedes configurar para el Modo App y guardar como una aplicación.

## 

​

Trabajar con aplicaciones

Las acciones coinciden con el panel Flujos de trabajo para la lista filtrada:

  * Haz clic en una aplicación para abrirla.
  * Agregar a marcadores, renombrar, eliminar, duplicar y arrastrar se comportan de la misma manera que con los flujos de trabajo normales.
  * En el menú contextual, **Duplicar** siempre está disponible. **Insertar** está disponible fuera del Modo App.

Para ejecutar realmente una aplicación en la interfaz lineal simplificada, ábrela y entra en el Modo App. Consulta [Modo App](https://docs.comfy.org/es/interface/app-mode) para crear entradas y salidas, previsualizar el diseño y alternar entre la edición del gráfico y la vista estilo aplicación.

## 

​

Cómo se relacionan Aplicaciones con Flujos de trabajo y Plantillas

Superficie| Qué lista  
---|---  
[Flujos de trabajo](https://docs.comfy.org/es/interface/workflows)| Gráficos guardados normales (y pestañas abiertas), normalmente `.json`  
**Aplicaciones** (esta página)| Aplicaciones empaquetadas que terminan en `.app.json`  
[Plantillas](https://docs.comfy.org/es/interface/features/template)| Gráficos iniciales oficiales y de la comunidad desde **Explorar plantillas** , no tu biblioteca local de aplicaciones  
  
## 

​

Páginas relacionadas

  * [Modo App](https://docs.comfy.org/es/interface/app-mode)
  * [Flujos de trabajo](https://docs.comfy.org/es/interface/workflows)
  * [Plantillas](https://docs.comfy.org/es/interface/features/template)
  * [Resumen de la interfaz](https://docs.comfy.org/es/interface/overview)



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/interface/apps.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/interface/apps)

[Flujos de trabajo](https://docs.comfy.org/es/interface/workflows)[Historial de trabajos](https://docs.comfy.org/es/interface/job-history)
