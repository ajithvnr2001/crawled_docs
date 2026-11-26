---
url: https://docs.comfy.org/es/installation/desktop/usage/settings/
title: Configuraciones de Comfy Desktop - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-26T17:36:33.089987+00:00
---

# Configuraciones de Comfy Desktop - ComfyUI

> Source: https://docs.comfy.org/es/installation/desktop/usage/settings/

## En esta página

Volver arriba

  * Abrir Configuraciones de Escritorio
  * Configurar tus preferencias
    * Activar las funciones beta
  * Actualizar Comfy Desktop
    * Dejar que las actualizaciones se instalen solas
    * Actualizar desde la barra lateral
    * Buscar actualizaciones tú mismo
  * Elegir carpetas compartidas y la ubicación de instalación
  * Configurar espejos y aceleración por hardware
    * Conservar la caché de descargas
  * Encontrar el registro de la aplicación



Guía de uso

# Configuraciones de Comfy Desktop

Copiar páginaCopiar página

Cambia las configuraciones de Comfy Desktop: actualiza la app, define carpetas compartidas, ubicación de instalación, espejos, caché de descargas y registro.

Copiar páginaCopiar página

Comfy Desktop ejecuta tus compilaciones de ComfyUI, y **Configuraciones de Escritorio** contiene las opciones que afectan a todas ellas a la vez, como las carpetas que todas las compilaciones comparten para los modelos o el espejo que usan las descargas de paquetes. En cambio, las configuraciones de una compilación individual, como sus propias carpetas o argumentos de inicio, están en la página de esa compilación. Usa **Configuraciones de Escritorio** para actualizar Comfy Desktop, elegir carpetas compartidas y la ubicación de instalación predeterminada, configurar espejos y la caché de descargas, activar funciones beta y encontrar el registro de la aplicación.

## Abrir Configuraciones de Escritorio

  * En la parte inferior de la **barra lateral** , haz clic en **Desktop settings**. En una ventana que ejecuta ComfyUI, también puedes abrir el **Menú** de la **barra de título** y seleccionar **Desktop settings**. Consulta [Cómo moverte por Comfy Desktop](https://docs.comfy.org/es/installation/desktop/usage/overview#ubica-la-barra-lateral) para la **barra lateral** y la **barra de título**.

![La página Builds con la fila Desktop settings resaltada en la parte inferior de la barra lateral](https://mintcdn.com/dripart/HtsWGj9PL-oHaM8n/images/desktop/usage/comfy_desktop_settings_00_menu.png?fit=max&auto=format&n=HtsWGj9PL-oHaM8n&q=85&s=fe218501a37ba11b0fa56252ca4882a7) La ventana **Desktop settings** tiene cinco pestañas a la izquierda: **Preferences** , **Updates** , **Folders** , **Advanced** y **Logs**. Haz clic en una pestaña para cambiar a ella.

## Configurar tus preferencias

La pestaña **Preferences** configura el idioma de la aplicación y cómo se comporta Comfy Desktop cuando cierras ventanas o inicias compilaciones. ![Pestaña Preferences: Language establecido en English, los interruptores de App behavior, Share anonymous usage telemetry y Opt in to beta features en Privacy, y la tarjeta Comfy Desktop en Community](https://mintcdn.com/dripart/HtsWGj9PL-oHaM8n/images/desktop/usage/comfy_desktop_settings_01_preferences.png?fit=max&auto=format&n=HtsWGj9PL-oHaM8n&q=85&s=c7b8602a403358ba90b70d8d55a827f9)

  * **Language** : el idioma de Comfy Desktop. Selecciona **English** o **简体中文**.

En **App behavior** :

Configuración| Predeterminado| Qué hace  
---|---|---  
**Confirm before closing a window**|  Off| Pregunta antes de cerrar una ventana cuando eso detiene ComfyUI o cierra Comfy Desktop.  
**Warn before running multiple builds**|  On| Muestra una advertencia antes de que inicies otra compilación local de ComfyUI mientras una está en ejecución o iniciándose.  
**Hide Cloud from the build picker**|  Off| Oculta la fila de Comfy Cloud de **Home**. Comfy Cloud sigue funcionando y puedes desactivar el interruptor de nuevo en cualquier momento.  
  
En **Privacy** :

  * **Share anonymous usage telemetry** : envía datos de uso anónimos. El interruptor aparece activado hasta que lo desactives.
  * **Opt in to beta features** : permite que Comfy Desktop active funciones de ComfyUI en fase temprana en tus compilaciones. Consulta Activar las funciones beta.

En **Community** , la tarjeta **Comfy Desktop** abre el [repositorio de Comfy Desktop en GitHub](https://github.com/Comfy-Org/Comfy-Desktop).

### Activar las funciones beta

Con **Opt in to beta features** activado, ayudas a probar funciones de ComfyUI antes de que se publiquen. Cuando el interruptor está activado, Comfy Desktop puede agregar uno de estos argumentos de inicio cuando inicia una compilación en esta computadora: `--enable-asset-hashing`, `--disable-assets` o `--enable-agent`. Solo agrega un argumento cuando la versión de ComfyUI de la compilación lo admite. Si ya estableciste ese argumento o su opuesto en los argumentos de inicio de la compilación, Comfy Desktop deja los tuyos como están. Si nunca cambiaste el interruptor, sigue tu respuesta a **Help improve Comfy by sharing anonymous usage data.** durante la configuración inicial. Para activarlo:

  1. En la pestaña **Preferences** , activa **Opt in to beta features**.
  2. Si el interruptor no se activa, confirma primero el uso compartido de datos: desactiva **Share anonymous usage telemetry** y vuelve a activarlo. Luego activa **Opt in to beta features**.

Cuando una compilación se inicia con una función beta, un aviso en su **barra de título** dice **A beta feature is on** o **The beta is on**. Haz clic en **Got it** para cerrarlo, o en **Settings** para abrir esta pestaña en el interruptor beta. Cuando una función beta está desactivada para una compilación, el aviso dice **A beta feature is off** o **The beta is off**. Para ver qué argumentos agregó una función beta, abre la [pestaña **Startup arguments**](https://docs.comfy.org/es/installation/desktop/usage/instance-management#set-startup-arguments) de la compilación y haz clic en la píldora **+N beta**. Enumera los argumentos en **Added for this session** o **Eligible for next launch** , y **Manage beta features** abre esta pestaña en el interruptor beta.

## Actualizar Comfy Desktop

Comfy Desktop busca actualizaciones de sí mismo 2 segundos después de iniciarse y luego cada 10 minutos. Comfy Desktop no tiene un canal de actualización que elegir. El canal de actualización en la página de una compilación es para ComfyUI en esa compilación: consulta [Actualizar ComfyUI](https://docs.comfy.org/es/installation/desktop/usage/instance-management#update-comfyui).

En Linux, cómo se actualiza Comfy Desktop depende de si instalaste el paquete `.deb`, el AppImage o una copia del código fuente. Consulta [Actualizar en Linux](https://docs.comfy.org/es/installation/desktop/overview#instalar-comfy-desktop-para-tu-sistema-operativo).

### Dejar que las actualizaciones se instalen solas

La opción **Automatically install Desktop updates** en la pestaña **Updates** está activada de forma predeterminada. Cuando una búsqueda encuentra una actualización, Comfy Desktop la descarga y la instala:

  * En macOS y Linux, cuando salgas de Comfy Desktop.
  * En Windows, la próxima vez que inicies Comfy Desktop.

Cuando el interruptor está desactivado, una actualización se instala solo cuando haces clic en **Restart & update**.

### Actualizar desde la barra lateral

Cuando hay una actualización disponible, una entrada en la parte inferior de la **barra lateral** muestra su estado:

La entrada dice| Haz clic para  
---|---  
**Desktop update**|  Abrir el diálogo **Desktop update available**. Haz clic en **Download**.  
**Downloading update…**|  Abrir **Configuraciones de Escritorio** en la pestaña **Updates** , donde se muestra el progreso de la descarga.  
**Desktop update ready**|  Abrir el diálogo **Desktop update ready**. Haz clic en **Restart & update** para reiniciar con la actualización.  
  
### Buscar actualizaciones tú mismo

  1. Abre **Configuraciones de Escritorio** y haz clic en la pestaña **Updates**.
  2. Haz clic en **Check for updates**.
  3. Si la pestaña dice **Update available** , haz clic en **Download**.
  4. Cuando la pestaña diga **Update ready to install** , haz clic en **Restart & update**.

Comfy Desktop se reinicia con la actualización. La actualización se completó cuando la pestaña **Updates** dice **Comfy Desktop is up to date** y **Installed** muestra la versión que descargaste. ![Pestaña Updates mostrando Comfy Desktop is up to date, con la versión instalada, el botón Check for updates y el interruptor Automatically install Desktop updates](https://mintcdn.com/dripart/HtsWGj9PL-oHaM8n/images/desktop/usage/comfy_desktop_settings_02_updates.png?fit=max&auto=format&n=HtsWGj9PL-oHaM8n&q=85&s=9ede3287ce6d57b57b80142f13bb69bd)

## Elegir carpetas compartidas y la ubicación de instalación

Las carpetas compartidas permiten que cada instalación use los mismos modelos, entradas y salidas, así que descargas un modelo una vez en lugar de una vez por instalación. La pestaña **Folders** configura estas carpetas y la carpeta donde Comfy Desktop sugiere colocar las instalaciones que creas. ![Pestaña Folders: Default install location con su ruta, la lista Shared folders con las filas Models, Input y Output, la etiqueta Downloads, Use for downloads y Add models folder, luego Remove Comfy Desktop data](https://mintcdn.com/dripart/HtsWGj9PL-oHaM8n/images/desktop/usage/comfy_desktop_settings_03_storage.png?fit=max&auto=format&n=HtsWGj9PL-oHaM8n&q=85&s=c1c1c1e9f85f3343d0cdaf2f544137ff) En cada fila de carpeta, haz clic en la ruta para abrir la carpeta, o haz clic en el icono de carpeta para elegir otra carpeta.

  * **Default install location** : la carpeta principal que Comfy Desktop sugiere cuando creas una instalación. Cambiarla no mueve las instalaciones existentes.
  * **Shared folders** : una lista de carpetas **Models** , **Input** y **Output**. Cada instalación las usa de forma predeterminada. Para cambiar eso en una instalación, consulta [Elegir qué carpetas usa la instalación](https://docs.comfy.org/es/installation/desktop/usage/instance-management#choose-which-folders-the-build-uses).

Para administrar las carpetas compartidas de modelos:

  * **Agregar una carpeta de modelos** : haz clic en **Add models folder** y elige la carpeta.
  * **Elegir dónde descargar los modelos** : en una fila **Models** , haz clic en **Use for downloads**. Esa fila pasa a tener la etiqueta **Downloads**. Una instalación puede elegir su propia carpeta de descargas en su lugar. Consulta [Dónde se guardan las descargas](https://docs.comfy.org/es/installation/desktop/usage/downloads#d%C3%B3nde-se-guardan-las-descargas).
  * **Eliminar una carpeta de modelos** : haz clic en el menú **⋯** de la fila, selecciona **Remove** y confirma. Los archivos permanecen en el disco. La carpeta con la etiqueta **Downloads** no tiene menú **⋯** , así que primero elige otra carpeta de descargas. No puedes eliminar las filas **Input** y **Output**.

De forma predeterminada, las carpetas son:

Carpeta| macOS y Linux| Windows  
---|---|---  
**Default install location**| `~/ComfyUI-Installs`| `%LOCALAPPDATA%\Comfy-Desktop\ComfyUI-Installs`  
Carpetas compartidas **Models** , **Input** y **Output**| `~/ComfyUI-Shared/models`, `input`, `output`| `%LOCALAPPDATA%\Comfy-Desktop\ComfyUI-Shared\models`, `input`, `output`  
  
En Windows, si tu carpeta de usuario ya tenía `ComfyUI-Installs` o `ComfyUI-Shared`, Comfy Desktop sigue usando esas. Si instalaste Comfy Desktop en una unidad distinta de la unidad del sistema, las carpetas están en `<drive>:\Comfy-Desktop` en su lugar.

En macOS y Linux, la pestaña **Folders** también tiene **Remove Comfy Desktop data** , que elimina los registros, cachés y archivos temporales de la aplicación antes de desinstalarla. Consulta [Desinstalar Comfy Desktop en macOS](https://docs.comfy.org/es/installation/desktop/overview#desinstalar-comfy-desktop) o [eliminar los datos sobrantes en Linux](https://docs.comfy.org/es/installation/desktop/overview#desinstalar-comfy-desktop).

## Configurar espejos y aceleración por hardware

Si las descargas desde pypi.org o github.com son lentas en tu ubicación, apunta Comfy Desktop a un espejo en la pestaña **Advanced**. ![Pestaña Advanced: URL del espejo de PyPI, Use Chinese mirrors \(Git & PyPI\), Use hardware acceleration y la sección Cache con el directorio de caché](https://mintcdn.com/dripart/HtsWGj9PL-oHaM8n/images/desktop/usage/comfy_desktop_settings_04_advanced.png?fit=max&auto=format&n=HtsWGj9PL-oHaM8n&q=85&s=a8a0dffff51604ac3d52282a4ed1deaf)

  * **PyPI mirror URL** : un índice de paquetes de Python, como `https://mirrors.aliyun.com/pypi/simple/`. Comfy Desktop instala los paquetes de Python desde este índice y usa pypi.org como índice adicional. Está vacío de forma predeterminada.
  * **Use Chinese mirrors (Git & PyPI)**: desactivado de forma predeterminada. Cuando está activado, los repositorios Git se clonan desde gitcode.com en lugar de github.com, y los paquetes de Python provienen de mirrors.aliyun.com y mirrors.cloud.tencent.com en lugar de pypi.org. Cuando el idioma de la aplicación es chino, este interruptor aparece en la pestaña **Preferences** , dentro de **App behavior**. Cuando el idioma de tu sistema es chino, la instalación también pregunta **Enable Chinese mirrors?**.
  * **Use hardware acceleration** : activado de forma predeterminada. Usa la GPU para renderizar Comfy Desktop. Reinicia Comfy Desktop para que un cambio surta efecto.



### Conservar la caché de descargas

Cuando instalas una compilación Standalone, Comfy Desktop descarga un paquete de ComfyUI en la carpeta de caché que se muestra en **Cache** , en la pestaña **Advanced**. De forma predeterminada, la carpeta se llama `download-cache`. Si instalas el mismo paquete otra vez, la instalación muestra **Using cached download** y omite la descarga. Comfy Desktop guarda solo el paquete más reciente en esta carpeta. Cuando termina una descarga, elimina las demás subcarpetas dentro de la carpeta de caché, así que no guardes nada más ahí. Haz clic en el icono de carpeta para elegir otra carpeta.

## Encontrar el registro de la aplicación

El registro de la aplicación registra lo que hace Comfy Desktop, incluida la salida cuando una compilación se instala o se inicia. Adjúntalo cuando reportes un problema en el [rastreador de problemas de Comfy Desktop](https://github.com/Comfy-Org/Comfy-Desktop/issues). ![Pestaña Registros con la sección Diagnóstico y el botón Abrir carpeta de registros](https://mintcdn.com/dripart/HtsWGj9PL-oHaM8n/images/desktop/usage/comfy_desktop_settings_05_logs.png?fit=max&auto=format&n=HtsWGj9PL-oHaM8n&q=85&s=1bbd4ef749d3b545631ef195bcf3c143)

  * En la pestaña **Registros** , dentro de **Diagnóstico** , haz clic en **Abrir carpeta de registros**.

La carpeta contiene `app.log` de la sesión actual. En cada inicio, y cuando `app.log` supera los 5 MB, Comfy Desktop cambia el nombre del archivo antiguo a `app.log_<timestamp>.log` y conserva hasta 50 de ellos. Elige el archivo de la sesión en la que ocurrió el problema.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/installation/desktop/usage/settings.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/installation/desktop/usage/settings)

[Administrar](https://docs.comfy.org/es/installation/desktop/usage/manage)[Pruebas de rendimiento](https://docs.comfy.org/es/installation/desktop/usage/performance-tests)
