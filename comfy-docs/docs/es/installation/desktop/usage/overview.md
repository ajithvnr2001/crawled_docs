---
url: https://docs.comfy.org/es/installation/desktop/usage/overview/
title: C\u00f3mo usar Comfy Desktop - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-25T12:24:48.635016+00:00
---

# Cómo usar Comfy Desktop - ComfyUI

> Source: https://docs.comfy.org/es/installation/desktop/usage/overview/

## En esta página

  * Características principales
  * Descripción general del Panel
    * Menú de la aplicación
    * Selector de instancias
    * Botones del lado derecho
    * Buscar
    * Selector (Lista de instancias)
  * Retroalimentación y problemas



Guía de uso

# Cómo usar Comfy Desktop

Copiar páginaCopiar página

Descripción general de Comfy Desktop: crear instalaciones nuevas, administrar instancias y más

Copiar páginaCopiar página

Comfy Desktop es la aplicación oficial de escritorio para **ComfyUI**. Gestiona todo por ti: instala ComfyUI, lo mantiene actualizado y te permite ejecutar varias configuraciones independientes en paralelo. Para entender la relación: **Comfy Desktop** es la aplicación que administra e inicia instancias de **ComfyUI**. No instalas ComfyUI por separado: Comfy Desktop se encarga de la instalación, el entorno de Python y las dependencias de cada instancia de forma automática.

### 

​

Características principales

  * **[Gestión de múltiples instancias](https://docs.comfy.org/es/installation/desktop/usage/instance-management)** : ejecuta varias instancias de ComfyUI en paralelo, cada una con su propia versión, nodos personalizados y configuración
  * **[Snapshots](https://docs.comfy.org/es/installation/desktop/usage/manage#pesta%C3%B1a-instant%C3%A1neas)** : guarda y restaura el estado completo de una instancia (versión de ComfyUI, nodos personalizados, paquetes de Python), lo que facilita revertir o reproducir un entorno
  * **[Almacenamiento compartido](https://docs.comfy.org/es/installation/desktop/usage/settings#almacenamiento)** : los modelos se comparten entre todas las instancias de forma predeterminada, lo que ahorra espacio en disco. También puedes agregar carpetas de modelos externas
  * **Actualizaciones automáticas** : el control **Desktop Update** de la barra de título actualiza Comfy Desktop. Usa la pestaña [Actualizar](https://docs.comfy.org/es/installation/desktop/usage/manage#pesta%C3%B1a-actualizar) del panel Administrar para actualizar cada instancia de ComfyUI.
  * **Integración con la nube** : inicia o conéctate a instancias de Comfy Cloud directamente desde la vista Chooser
  * **[Rastrear instalaciones existentes](https://docs.comfy.org/es/installation/desktop/usage/instance-management#seguimiento-de-una-instalaci%C3%B3n-existente)** : agrega tus instalaciones existentes de ComfyUI, ya sean portables o clonadas con git, a Comfy Desktop para una gestión unificada

Esta guía explica cómo usar estas funciones.

## 

​

Descripción general del Panel

La ventana de Comfy Desktop se divide en varias áreas clave. La siguiente imagen señala las partes principales del Panel: ![Panel de Comfy Desktop con Nueva instancia, tarjeta de instancia local y Comfy Cloud](https://mintcdn.com/dripart/N4LZwJLSpBN0lv19/images/desktop/interface/interface_desktop_dashboard.png?fit=max&auto=format&n=N4LZwJLSpBN0lv19&q=85&s=dfa65d60903d534faa4805ea7266fc4a)

### 

​

Menú de la aplicación

El menú de hamburguesa (☰) de la esquina superior izquierda abre el menú de la aplicación, que contiene todas las acciones a nivel de aplicación: ![Menú de la aplicación abierto desde la barra de título, incluyendo Pruebas de rendimiento, Benchmarks y Configuraciones de Escritorio](https://mintcdn.com/dripart/N4LZwJLSpBN0lv19/images/desktop/usage/comfy_desktop_app_menu.png?fit=max&auto=format&n=N4LZwJLSpBN0lv19&q=85&s=9d7299fff5dc05a214fcadf5f46870ef)

  * **Abrir el Panel** : abre el Panel en una nueva ventana. Las instancias que están en ejecución siguen ejecutándose.
  * **Nueva instancia** y **Añadir instancia existente** : crea una nueva instancia, o da seguimiento a una instalación de ComfyUI que ya tengas.
  * **Cargar instantánea** : crea una instancia a partir de un archivo de instantánea que alguien compartió contigo.
  * **Iniciar sesión** : inicia sesión en tu cuenta de Comfy. Esta entrada solo aparece mientras no hayas iniciado sesión.
  * **Pruebas de rendimiento** : ejecuta flujos de trabajo cronometrados contra una instancia. Consulta [Pruebas de rendimiento y Benchmarks](https://docs.comfy.org/es/installation/desktop/usage/performance-tests).
  * **Benchmarks** : compara los resultados guardados de las pruebas de rendimiento entre hardware, flujos de trabajo e instancias.
  * **Configuraciones de Escritorio** : configuración global para actualizaciones automáticas, proxy/espejo, almacenamiento compartido y ubicaciones de datos.
  * **Enviar retroalimentación** : abre el panel de retroalimentación.
  * **Cerrar ventana** y **Salir de Desktop** : cierra la ventana actual o sale de la aplicación. Cerrar la ventana de una instancia detiene la instancia de ComfyUI que ejecuta, y cerrar la última ventana cierra Comfy Desktop.

Dos entradas aparecen solo en contexto: **Restablecer zoom (N%)** una vez que la vista de ComfyUI tiene zoom aplicado, y **Omitir la configuración inicial** durante la configuración de primer uso. Mientras la configuración de primer uso está en pantalla, **Omitir la configuración inicial** es la única entrada del menú. En macOS, la app también mantiene una barra de menús del sistema con los menús estándar de la app, Editar y Ventana. Las compilaciones para Windows y Linux no tienen barra de menús del sistema.

## Configuraciones

Configuración global: actualizaciones automáticas, proxy/espejo, almacenamiento compartido y ubicaciones de datos.

## Pruebas de rendimiento

Mide la velocidad de los flujos de trabajo en una instancia y luego compara las ejecuciones entre distintos hardware.

### 

​

Selector de instancias

La píldora central muestra el nombre de tu instancia de ComfyUI activa. Haz clic en ella para abrir el **Selector de instancias** , un popover que lista todas las instancias instaladas, muestra su estado de ejecución y te permite cambiar entre ellas o iniciar una nueva. Cuando hay una nueva versión de ComfyUI disponible para esa instancia, la píldora también incluye un chip de **Actualizar** ; haz clic en el chip para actualizar la instancia sin abrir el selector.

## Administrar instalaciones

Inicia, actualiza, crea instantáneas y configura tus instalaciones a través del panel Administrar.

### 

​

Botones del lado derecho

![Controles del lado derecho de la barra de título: Novedades \(campana\), Retroalimentación y Descargas](https://mintcdn.com/dripart/N4LZwJLSpBN0lv19/images/desktop/usage/title_bar_trailing.png?fit=max&auto=format&n=N4LZwJLSpBN0lv19&q=85&s=c6f57d6e2cf179a5ee7952395e3b59a5) Los controles agrupados en el lado derecho de la barra de título dan acceso rápido a:

  * **Actualización de Desktop** : cuando hay una nueva versión de Comfy Desktop disponible, aparece una píldora aquí. Haz clic para descargar y aplicar la actualización.
  * **Restablecer zoom** : aparece una píldora con el porcentaje de zoom actual mientras la vista de ComfyUI tiene un zoom distinto de 100%. Haz clic en ella para volver al 100%.
  * **Novedades** : abre el panel de anuncios. Los anuncios cubren nuevas funciones de ComfyUI y lanzamientos de productos de Comfy, con un video corto, lo más destacado y enlaces para ver los detalles. La campana muestra un punto mientras haya un anuncio que no hayas abierto, y el punto desaparece en cuanto abres el panel.
  * **Retroalimentación** : envía retroalimentación al equipo de Comfy Desktop.
  * **Descargas** : abre la bandeja de descargas. La insignia muestra cuántas descargas están en curso y marca las descargas fallidas y las no abiertas. La bandeja te permite reintentar una descarga fallida o cancelar una que esté en curso; selecciona **Ver todas las descargas** para ver la lista completa, donde las descargas también se pueden pausar y reanudar.



### 

​

Buscar

La caja de búsqueda te permite filtrar tus instancias instaladas por nombre, lo que facilita encontrar una configuración específica cuando tienes muchas.

### 

​

Selector (Lista de instancias)

El área principal del Panel, llamada el **Selector** , muestra todas tus instancias de ComfyUI como tarjetas. **Haz clic en cualquier tarjeta de instancia para iniciar o cambiar a esa instancia.** Desde aquí puedes:

  * **＋ Nueva instancia** : crea una nueva instancia de ComfyUI independiente.
  * **Comfy Cloud** : conéctate a una instancia en la nube o iníciala. La tarjeta puede mostrar una píldora **PRUEBA GRATIS** cuando hay ejecuciones gratuitas de Cloud disponibles.
  * **Chip de cuenta** (arriba a la derecha): inicia sesión con tu cuenta de Comfy. Una vez que hayas iniciado sesión, el chip muestra tu avatar y tu correo electrónico, y aparece un selector de espacios de trabajo encima de la cuadrícula.
  * **Compilaciones del espacio de trabajo** : con la sesión iniciada, las ComfyUI Builds publicadas en el espacio de trabajo seleccionado se pueden instalar desde el flujo de Nueva instancia. Consulta [Espacios de trabajo y ComfyUI Builds](https://docs.comfy.org/es/installation/desktop/usage/workspaces-and-builds).
  * **Tarjetas de instancias existentes** : cada tarjeta muestra el nombre, el estado y el tipo de la instancia. Haz clic derecho (o haz clic en el ícono ⋮) para administrar, actualizar, crear una instantánea o eliminar la instancia.



## Administración de instancias

Crea, renombra, edita y elimina instancias de ComfyUI.

## 

​

Retroalimentación y problemas

¿Encontraste un error o tienes una sugerencia? Comfy Desktop es de código abierto. Puedes reportar problemas y consultar las funciones planificadas aquí:

  * **Problemas de Comfy Desktop** : [github.com/Comfy-Org/Comfy-Desktop/issues](https://github.com/Comfy-Org/Comfy-Desktop/issues)
  * **Problemas de la documentación** : [github.com/Comfy-Org/docs/issues](https://github.com/Comfy-Org/docs/issues)

Para preguntas generales sobre ComfyUI, visita las [ComfyUI GitHub Discussions](https://github.com/Comfy-Org/ComfyUI/discussions) o únete al [ComfyUI Discord](https://www.comfy.org/discord).

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/installation/desktop/usage/overview.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/installation/desktop/usage/overview)

[Linux](https://docs.comfy.org/es/installation/desktop/linux)[Instancia](https://docs.comfy.org/es/installation/desktop/usage/instance-management)
