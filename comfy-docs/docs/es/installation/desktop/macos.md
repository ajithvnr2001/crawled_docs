---
url: https://docs.comfy.org/es/installation/desktop/macos/
title: Comfy Desktop para macOS - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-25T12:24:48.242836+00:00
---

# Comfy Desktop para macOS - ComfyUI

> Source: https://docs.comfy.org/es/installation/desktop/macos/

## En esta página

  * Requisitos del sistema
  * Instalación
  * Actualizar Comfy Desktop
  * Actualización rápida
  * Actualización manual desde Configuraciones
  * Desinstalar
    * Eliminar Comfy Desktop
    * Lo que la desinstalación de la app NO elimina



Instalación

# Comfy Desktop para macOS

Copiar páginaCopiar página

Instala Comfy Desktop en macOS: requisitos del sistema, pasos de configuración, actualizaciones y una desinstalación limpia para ejecutar ComfyUI localmente en Macs con Apple Silicon.

Copiar páginaCopiar página

**Comfy Desktop** es un administrador de instalaciones múltiples que te permite ejecutar varias instancias de ComfyUI desde un único lanzador. Esta guía explica cómo instalar y desinstalar Comfy Desktop en macOS.

## 

​

Requisitos del sistema

  * **SO:** macOS 13 (Ventura) o posterior
  * **Hardware:** Apple Silicon (M1 o posterior)
  * **Espacio en disco:** al menos 4.85 GB recomendados por instalación



## Descargar Comfy Desktop

Descarga el instalador más reciente para macOS. La página detectará tu plataforma automáticamente.

## 

​

Instalación

  1. Abre el archivo `.dmg` descargado
  2. Arrastra **Comfy Desktop** a la carpeta **Aplicaciones**
  3. Ábrelo desde Launchpad o Spotlight

![Desktop MacOS](https://mintcdn.com/dripart/gG5z6ITsBp8xzLix/images/desktop/installation/mac_1_install.png?fit=max&auto=format&n=gG5z6ITsBp8xzLix&q=85&s=32a354755add8f6d72a0787b9ad42b67) La primera vez que lo abras, macOS podría mostrar una advertencia de seguridad. Ve a **Configuración del Sistema → Privacidad y seguridad** y haz clic en **Abrir de todos modos** para permitirlo.

**¿Ya usas el Comfy Desktop Clásico?** Comfy Desktop puede detectar y migrar automáticamente tu instalación existente. Tus nodos personalizados, flujos de trabajo, modelos y configuraciones se conservan, y Comfy Desktop respalda tu estado Clásico antes de iniciarse. La migración reutiliza tu carpeta de datos y tu entorno de Python existentes tal como están, así que haz tu propia copia de seguridad si necesitas una copia intacta.Aprende más en la guía [Migrar desde la versión Clásica](https://docs.comfy.org/es/installation/desktop/usage/migrate).

## Siguiente paso: usar Comfy Desktop

Una vez instalado, aprende a crear instancias, administrar instalaciones y configurar los ajustes.

## 

​

Actualizar Comfy Desktop

Comfy Desktop busca actualizaciones automáticamente y te permite administrarlas de dos maneras.

## 

​

Actualización rápida

Cuando hay una actualización disponible, aparece un botón **Desktop Update Ready** en la parte superior de la ventana: ![Botón Desktop Update Ready](https://mintcdn.com/dripart/gG5z6ITsBp8xzLix/images/desktop/installation/install_update_1.png?fit=max&auto=format&n=gG5z6ITsBp8xzLix&q=85&s=fc104f738021e738dd56c9b4f8fa64e5) Solo haz clic en el botón ① Desktop Update Ready y Comfy Desktop se reiniciará e instalará la actualización automáticamente.

## 

​

Actualización manual desde Configuraciones

También puedes buscar y administrar actualizaciones desde el panel de Configuraciones:

1

Abre las Configuraciones de Escritorio

![Abrir el menú de Configuraciones de Escritorio](https://mintcdn.com/dripart/gG5z6ITsBp8xzLix/images/desktop/installation/install_update_2-1.png?fit=max&auto=format&n=gG5z6ITsBp8xzLix&q=85&s=a43d379acfb8f89a4d4adab5ce63a920)

  1. **①** Haz clic en el menú de hamburguesa (arriba a la izquierda)
  2. **②** Selecciona **Configuraciones de Escritorio**



2

Panel de Actualizaciones

![Panel de Actualizaciones en Configuraciones de Escritorio](https://mintcdn.com/dripart/gG5z6ITsBp8xzLix/images/desktop/installation/install_update_2-2.png?fit=max&auto=format&n=gG5z6ITsBp8xzLix&q=85&s=f5e9af07392438b02f41d0a2211b6bd1)En el panel **Updates** :

  1. **① Updates** : haz clic en la pestaña Updates de la barra lateral
  2. **② Check for updates** : busca manualmente las actualizaciones disponibles
  3. **③ Restart & Update**: aparece cuando hay una nueva versión disponible; haz clic para reiniciar y actualizar
  4. **④ Automatically install Desktop updates** : actívalo o desactívalo para controlar las actualizaciones automáticas



## 

​

Desinstalar

### 

​

Eliminar Comfy Desktop

  1. Abre la carpeta **Aplicaciones** en Finder
  2. Haz clic derecho en **Comfy Desktop** y selecciona **Mover a la papelera**

![Desinstalar Comfy Desktop en macOS](https://mintcdn.com/dripart/gG5z6ITsBp8xzLix/images/desktop/installation/mac_2_uninstall.png?fit=max&auto=format&n=gG5z6ITsBp8xzLix&q=85&s=2b2704e427cfefa46b1a545ed55c498d)

### 

​

Lo que la desinstalación de la app NO elimina

Desinstalar Comfy Desktop solo elimina la aplicación del lanzador. Los siguientes datos **no** se eliminan y debes borrarlos manualmente si quieres una limpieza completa:

Datos| Ubicación predeterminada| Descripción  
---|---|---  
Instalaciones| `~/ComfyUI-Installs`| Cada instalación de ComfyUI que creaste (también se puede eliminar desde la app). Las rutas de instalación personalizadas tampoco se eliminan.  
Modelos y salidas compartidos| `~/ComfyUI-Shared`| Biblioteca de modelos compartida, directorios de entrada/salida  
Configuraciones y registro de la app| `~/Library/Application Support/Comfy Desktop`| Configuraciones y registros de instalación  
Registros| `~/Library/Logs/Comfy Desktop`| Registros de la app de escritorio (`app.log`)  
  
Los directorios enumerados arriba contienen tus **datos personales de ComfyUI** (modelos, salidas, configuraciones e instalaciones). **No** son archivos de la aplicación Comfy Desktop. Si los eliminas, tus datos se borrarán de forma permanente.

Para eliminar todo por completo:

  1. **Elimina la carpeta de datos de la app** : `~/Library/Application Support/Comfy Desktop`
  2. **Elimina la carpeta de registros** : `~/Library/Logs/Comfy Desktop`
  3. **Elimina las instalaciones individuales** desde la app, o borra manualmente `~/ComfyUI-Installs` junto con los directorios de instalación personalizados que hayas configurado
  4. **Elimina la biblioteca de modelos compartida** en `~/ComfyUI-Shared` (solo si ya no necesitas estos archivos)



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/installation/desktop/macos.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/installation/desktop/macos)

[Windows](https://docs.comfy.org/es/installation/desktop/windows)[Linux](https://docs.comfy.org/es/installation/desktop/linux)
