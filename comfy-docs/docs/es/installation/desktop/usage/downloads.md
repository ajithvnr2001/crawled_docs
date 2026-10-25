---
url: https://docs.comfy.org/es/installation/desktop/usage/downloads/
title: Descargas de modelos en Comfy Desktop - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-25T12:24:48.586400+00:00
---

# Descargas de modelos en Comfy Desktop - ComfyUI

> Source: https://docs.comfy.org/es/installation/desktop/usage/downloads/

## En esta página

  * Lo que aparece en la lista de descargas
  * La bandeja de Descargas
  * La vista completa de Descargas
  * Salir con descargas en progreso
  * Dónde se guardan las descargas



Guía de uso

# Descargas de modelos en Comfy Desktop

Copiar páginaCopiar página

Sigue las descargas activas y recientes de modelos y salidas, reinténtalas o pausálas, y consulta dónde guarda Comfy Desktop cada archivo.

Copiar páginaCopiar página

Comfy Desktop descarga los modelos para tus instancias y lleva el seguimiento de cada transferencia en un solo lugar. Cuando una instancia de ComfyUI solicita un modelo que todavía no está en el disco, Comfy Desktop se encarga de la descarga y guarda el archivo en el directorio de modelos de la instancia, así que no tienes que colocarlo a mano. Abre la bandeja **Descargas** desde la barra de título para seguir las descargas activas, reintentar una descarga fallida o ir a la carpeta donde quedó un archivo finalizado.

## 

​

Lo que aparece en la lista de descargas

  * **Modelos faltantes** : cuando ComfyUI reporta modelos faltantes en el diálogo de modelos faltantes o en la pestaña **Errores** del panel del lado derecho, la acción de descarga se gestiona a través de Comfy Desktop. Cada archivo se guarda en la carpeta de modelos correspondiente, como `checkpoints`, `diffusion_models`, `text_encoders`, `loras` o `vae`. Los tipos de archivo de modelo admitidos son `.safetensors`, `.sft`, `.ckpt`, `.pth` y `.pt`.
  * **Modelos de plantilla** : cuando configuras una instancia a partir de una plantilla de inicio, los modelos que esa plantilla necesita se descargan en segundo plano y aparecen en la bandeja como cualquier otra descarga. La pantalla de progreso mantiene visible el paso de descarga de modelos hasta que finalicen. Si prefieres empezar de inmediato, **Saltar y abrir ComfyUI** en esa pantalla abre ComfyUI enseguida y las descargas siguen ejecutándose en la bandeja.
  * **Salidas de instancias remotas** : cuando ejecutas un flujo de trabajo en una instancia remota o de Cloud, las salidas finalizadas se descargan automáticamente en tu directorio de salida local.



## 

​

La bandeja de Descargas

Haz clic en el botón **Descargas** de los controles finales de la barra de título para abrir la bandeja. Las descargas se listan con las más recientes primero, etiquetadas con su carpeta de modelo y su nombre de archivo, y las filas activas muestran el tamaño transferido, el porcentaje, la velocidad y el tiempo restante estimado. ![Bandeja de Descargas abierta desde la barra de título de Comfy Desktop, con las descargas de modelos listadas junto a su carpeta y su progreso](https://mintcdn.com/dripart/u_e-u6-s3jR2i6kZ/images/desktop/usage/downloads_01_tray.png?fit=max&auto=format&n=u_e-u6-s3jR2i6kZ&q=85&s=477a8b952fbbebe27cb71398d6945886) El botón muestra una insignia con el número de descargas activas. Cuando no se está descargando nada, en su lugar señala las descargas que fallaron y no has revisado, o las que finalizaron y aún no has abierto. Cada fila tiene estas acciones:

  * **Haz clic en una fila finalizada** para abrir la carpeta que contiene el archivo (Mostrar en Finder, Mostrar en Explorer o Mostrar en carpeta, según tu sistema).
  * **Reintentar** una descarga fallida o cancelada.
  * **✕** para cancelar una descarga activa, o eliminar una finalizada de la lista.

**Ver todas las descargas** , en la parte inferior de la bandeja, abre la vista completa de descargas.

## 

​

La vista completa de Descargas

La vista completa conserva el historial de descargas de la aplicación y añade los controles que no caben en la bandeja:

  * Filtra la lista por **Todas** , **Activas** , **Completadas** o **Fallidas**.
  * **Pausar** una descarga activa y **Reanudar** una que esté en pausa.
  * **Reintentar** una descarga fallida o cancelada.
  * Abrir la carpeta del archivo o eliminar una sola fila.
  * **Limpiar finalizadas** para eliminar todas las filas finalizadas a la vez.

El pie de página muestra el recuento de las descargas activas y completadas que aparecen en la lista. ![Vista completa de Descargas con descargas en pausa, cada una con una acción Reanudar, y el recuento de activas en el pie de página](https://mintcdn.com/dripart/u_e-u6-s3jR2i6kZ/images/desktop/usage/downloads_02_full_view.png?fit=max&auto=format&n=u_e-u6-s3jR2i6kZ&q=85&s=25934a96dcf459b2f3cc53688b668e8f)

## 

​

Salir con descargas en progreso

Las descargas de modelos se pueden reanudar. Si sales de Comfy Desktop mientras se está ejecutando una transferencia de modelo, los bytes ya recibidos se conservan y, en el siguiente inicio, la transferencia vuelve como una fila en pausa en la bandeja Descargas. Abre **Ver todas las descargas** para **Reanudarla** desde donde se detuvo, o cancélala para descartar el archivo parcial. Las descargas de salida de instancias remotas se transfieren por una ruta separada y no se reanudan después de salir. Cuando los modelos de una plantilla aún se están descargando, Comfy Desktop te pide que confirmes la salida, porque la configuración de la plantilla espera esos archivos:

  * **Salir de todos modos** : pone las descargas en pausa y sale. Las filas siguen ahí en el siguiente inicio.
  * **Seguir descargando** : cancela la salida y deja Comfy Desktop en ejecución. Esta es la opción predeterminada.

Las salidas que inicia Comfy Desktop por sí mismo, como instalar una actualización o reiniciar, omiten este aviso. También lo hace **Salir de Desktop** en el menú de la barra de título, que muestra su propia confirmación con las descargas activas. Las transferencias se ponen en pausa en cualquier caso y vuelven en el siguiente inicio.

## 

​

Dónde se guardan las descargas

Los archivos de modelo se escriben en el directorio de descargas de modelos de la instancia: el directorio de modelos compartido marcado como **DESCARGAS** (se configura con **Usar para descargas de modelos**) cuando la instancia incluye directorios de modelos compartidos; de lo contrario, en la carpeta `models` propia de la instancia. Los directorios compartidos se configuran en [Configuraciones de Escritorio](https://docs.comfy.org/es/installation/desktop/usage/settings#almacenamiento), y cada instancia puede excluirse de ellos en su panel **Administrar** , [pestaña Almacenamiento](https://docs.comfy.org/es/installation/desktop/usage/manage#pesta%C3%B1a-almacenamiento). Las salidas descargadas desde una instancia remota se guardan en la carpeta de salidas compartida cuando la instancia la utiliza; de lo contrario, en la carpeta de salidas propia de la instancia. Una instancia remota puede desactivar la descarga automática de salidas con **Descarga automática de salidas** en sus configuraciones de almacenamiento.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/installation/desktop/usage/downloads.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/installation/desktop/usage/downloads)

[Instantáneas](https://docs.comfy.org/es/installation/desktop/usage/snapshots)[Administrar](https://docs.comfy.org/es/installation/desktop/usage/manage)
