---
url: https://docs.comfy.org/es/installation/desktop/windows/
title: Comfy Desktop para Windows - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-25T12:24:48.832376+00:00
---

# Comfy Desktop para Windows - ComfyUI

> Source: https://docs.comfy.org/es/installation/desktop/windows/

## En esta página

  * Requisitos del sistema
  * Instalación
  * Actualizar Comfy Desktop
  * Actualización rápida
  * Actualización manual desde Configuraciones
  * Desinstalación
    * Eliminar Comfy Desktop
    * Lo que la desinstalación de la aplicación NO elimina



Instalación

# Comfy Desktop para Windows

Copiar páginaCopiar página

Instala Comfy Desktop en Windows: requisitos del sistema, pasos de configuración, actualizaciones y una desinstalación limpia para ejecutar ComfyUI localmente en Windows 10 y versiones posteriores.

Copiar páginaCopiar página

**Comfy Desktop** es un administrador de instalaciones múltiples que te permite ejecutar varias instancias de ComfyUI desde un solo lanzador. Esta guía explica cómo instalar y desinstalar Comfy Desktop en Windows.

## 

​

Requisitos del sistema

  * **SO:** Windows 10 o posterior
  * **Arquitectura:** x64 o ARM64
  * **GPU:** Se recomienda una GPU dedicada (NVIDIA / AMD) para un buen rendimiento, pero no es obligatoria
  * **Espacio en disco:** Se recomienda al menos 4.85 GB por instalación



## Descargar Comfy Desktop

Descarga el instalador más reciente para Windows. La página detectará tu plataforma automáticamente.

## 

​

Instalación

Ejecuta el instalador `.exe` descargado (instalador NSIS) y sigue las instrucciones en pantalla. Después de la instalación, inicia Comfy Desktop desde el Menú Inicio o el acceso directo del escritorio. ![Configuración de Windows](https://mintcdn.com/dripart/cAVuyhdaebQHS2CS/images/desktop/installation/windows_1_install.png?fit=max&auto=format&n=cAVuyhdaebQHS2CS&q=85&s=2f32d2b272b240371c7b2290343cf400) La primera vez que abras la aplicación, la configuración inicial te pregunta cómo quieres ejecutar Comfy: en Comfy Cloud o instalado localmente en esta máquina. Consulta [Primer inicio](https://docs.comfy.org/es/installation/desktop/overview#primer-inicio) para conocer las opciones que recopila.

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

Desinstalación

### 

​

Eliminar Comfy Desktop

  1. Ve a **Configuración → Aplicaciones → Aplicaciones instaladas**
  2. Busca **Comfy Desktop** y haz clic en **Desinstalar**

![Desinstalar Comfy Desktop en Windows](https://mintcdn.com/dripart/cAVuyhdaebQHS2CS/images/desktop/installation/windows_2_uninstall.png?fit=max&auto=format&n=cAVuyhdaebQHS2CS&q=85&s=53de7983e9318d6aecad6e76a25c5efe)

### 

​

Lo que la desinstalación de la aplicación NO elimina

Desinstalar Comfy Desktop solo elimina la aplicación lanzadora en sí. Los siguientes datos **no** se eliminan y debes eliminarlos manualmente si quieres una limpieza completa:

Datos| Ubicación predeterminada| Descripción  
---|---|---  
Instalaciones| `%LOCALAPPDATA%\Comfy-Desktop\ComfyUI-Installs`| Cada instalación de ComfyUI que hayas creado (también se puede eliminar desde la aplicación). Las rutas de instalación personalizadas tampoco se eliminan. Las instalaciones más antiguas pueden seguir en `%USERPROFILE%\ComfyUI-Installs`.  
Modelos y salidas compartidos| `%LOCALAPPDATA%\Comfy-Desktop\ComfyUI-Shared`| Biblioteca de modelos compartida, directorios de entrada y salida. Las instalaciones más antiguas pueden seguir usando `%USERPROFILE%\ComfyUI-Shared`.  
Configuraciones y registro de la aplicación| `%APPDATA%\Comfy Desktop`| Configuraciones y registros de instalación  
Registros| `%APPDATA%\Comfy Desktop\logs`| Registros de la aplicación de escritorio (`app.log`)  
  
Los directorios enumerados arriba contienen tus **datos personales de ComfyUI** (modelos, salidas, configuraciones e instalaciones). **No** son archivos de la aplicación Comfy Desktop. Si los eliminas, borrarás tus datos de forma permanente.

Para eliminar todo por completo:

  1. **Elimina la carpeta de datos de la aplicación** : `%APPDATA%\Comfy Desktop`
  2. **Elimina las instalaciones individuales** desde la aplicación, o elimina manualmente `%LOCALAPPDATA%\Comfy-Desktop\ComfyUI-Installs` (o `%USERPROFILE%\ComfyUI-Installs` si es allí donde se crearon). Elimina también los directorios de instalación personalizados que hayas configurado
  3. **Elimina la biblioteca de modelos compartida** en `%LOCALAPPDATA%\Comfy-Desktop\ComfyUI-Shared` (o `%USERPROFILE%\ComfyUI-Shared`) solo si ya no necesitas estos archivos



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/installation/desktop/windows.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/installation/desktop/windows)

[Descripción general](https://docs.comfy.org/es/installation/desktop/overview)[macOS](https://docs.comfy.org/es/installation/desktop/macos)
