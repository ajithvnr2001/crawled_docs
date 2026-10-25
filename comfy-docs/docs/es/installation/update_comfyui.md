---
url: https://docs.comfy.org/es/installation/update_comfyui/
title: C\u00f3mo actualizar ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-25T12:24:49.060933+00:00
---

# Cómo actualizar ComfyUI - ComfyUI

> Source: https://docs.comfy.org/es/installation/update_comfyui/

## En esta página

  * ¿Cómo actualizar ComfyUI?
  * Tipos de versión de ComfyUI
  * ¿Qué se debe actualizar al actualizar ComfyUI?
  * Problemas comunes de actualización
    * Frontend, plantillas de flujos de trabajo o nodos faltantes o desactualizados después de las actualizaciones
    * Cómo actualizar correctamente las dependencias principales
    * Solución de problemas de actualización de dependencias principales
    * ¿Por qué no encuentro las nuevas funciones después de actualizar?
    * ¿Cómo cambiar entre la versión de desarrollo (nocturna) y la versión estable (release)?
    * ¿Qué hacer cuando ocurren errores después de actualizar?
    * ¿Cómo estar al día con las nuevas funciones?



Local (autoalojado)

# Cómo actualizar ComfyUI

Copiar páginaCopiar página

Actualiza ComfyUI en cualquier tipo de instalación: scripts de actualización de Portable, actualizaciones de Desktop y git pull para instalaciones manuales, además de soluciones para problemas comunes de actualización.

Copiar páginaCopiar página

Aunque ya hemos cubierto las actualizaciones de ComfyUI en los distintos métodos de instalación a lo largo de varias secciones, esta guía completa reúne todos los procedimientos de actualización para ayudarte a entender con claridad cómo actualizar ComfyUI.

## 

​

¿Cómo actualizar ComfyUI?

  * Portátil

  * Escritorio

  * Instalación manual




ComfyUI Portable incluye prácticos scripts de lote para actualizar fácilmente.

### 

​

Ubicación de los scripts de actualización

En la carpeta `update` dentro de tu directorio de instalación portátil, encontrarás los siguientes scripts de actualización:
    
    
    ComfyUI_windows_portable
    └─ 📂update
       ├── update.py
       ├── update_comfyui.bat                           // Actualizar a la última versión de desarrollo
       ├── update_comfyui_stable.bat                    // Actualizar a la última versión estable
       └── update_comfyui_and_python_dependencies.bat   // ⚠️ PELIGRO: Reinstala las dependencias - puede causar conflictos
    

Asegúrate de tener una conexión a internet estable durante las actualizaciones.

**⚠️ PELIGRO: ¡Usa`update_comfyui_and_python_dependencies.bat` con muchísima precaución!**Este script es más exhaustivo que las actualizaciones normales y hará lo siguiente:

  * ✅ Actualizar el propio código de ComfyUI
  * ✅ Actualizar PyTorch (para NVIDIA GPU CUDA 12.9)
  * ✅ Reinstalar TODAS las dependencias de Python

**Riesgos:**

  * Puede causar conflictos de dependencias con tu configuración actual
  * Puede romper nodos personalizados que dependen de versiones específicas de paquetes
  * Puede sobrescribir paquetes configurados manualmente

**⚠️ Usa este script solo cuando:**

  * Necesites solucionar problemas de dependencias
  * Vayas a realizar actualizaciones de versión mayor
  * Para actualizaciones diarias, usa `update_comfyui.bat` en su lugar

**Antes de ejecutar este script:**

  1. **Haz una copia de seguridad de toda tu instalación de ComfyUI**
  2. Documenta las versiones de paquetes personalizados que hayas instalado
  3. Prepárate para reinstalar los nodos personalizados si es necesario



Comfy Desktop usa Comfy Engine como administrador de paquetes para gestionar ComfyUI. Para actualizar el motor de ComfyUI, abre el [panel Administrar](https://docs.comfy.org/es/installation/desktop/usage/manage#pesta%C3%B1a-actualizar) y usa la pestaña Actualizar. Puedes elegir entre los canales de actualización **Estable** (predeterminado) y **Última en GitHub**.La aplicación de escritorio se actualiza automáticamente y es independiente de las actualizaciones del motor de ComfyUI.

ComfyUI instalado manualmente requiere comandos de Git para completar las actualizaciones.

### 

​

Requisitos previos a la actualización

Asegúrate de que tu sistema tenga [Git](https://git-scm.com/downloads) instalado y de que ComfyUI se haya instalado mediante Git clone.

### 

​

Pasos de actualización

1

Activar el entorno virtual

Primero, activa el entorno virtual de Python de ComfyUI (si estás usando uno):
    
    
    # Para entorno conda
    conda activate comfyui
    
    # Para entorno venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux  
    source venv/bin/activate
    

2

Obtener el código más reciente

Navega a tu directorio de instalación de ComfyUI y obtén el código más reciente:
    
    
    cd <ComfyUI-installation-path>
    git pull
    

3

Actualizar las dependencias

Instala o actualiza los paquetes de dependencias de ComfyUI:
    
    
    pip install -r requirements.txt
    

Asegúrate de estar en el entorno virtual de ComfyUI para evitar contaminar el entorno de Python a nivel del sistema

4

Reiniciar ComfyUI

Después de actualizar, reinicia ComfyUI:
    
    
    python main.py
    

### 

​

Cambiar de versión (opcional)

Para cambiar a una versión específica, usa estos comandos:
    
    
    # Ver el historial de commits
    git log --oneline
    
    # Cambiar a un commit específico
    git checkout <commit-hash>
    
    # Volver a la última versión
    git checkout master
    

Se recomiendan las actualizaciones regulares para obtener las últimas funciones y correcciones de seguridad, mientras que las versiones estables se recomiendan para la estabilidad del sistema

## 

​

Tipos de versión de ComfyUI

Según tu método de instalación, ComfyUI ofrece varias versiones de instalación. Los enlaces a continuación contienen las instrucciones de actualización para cada versión.

Comfy Desktop

Comfy Desktop permite la instalación independiente en **Windows** , **macOS (Apple Silicon)** y **Linux** (AppImage y `.deb`).

  * El código fuente está en [GitHub](https://github.com/Comfy-Org/Comfy-Desktop)



Las instalaciones de Desktop siguen por defecto la versión **estable** de ComfyUI. Si quieres cada última confirmación (commit), usa la versión portable o una instalación manual con git, o cambia el canal de actualización de la instancia a **Latest on GitHub**.

A continuación puedes elegir la instalación adecuada para tu sistema y hardware

  * Windows

  * macOS (Apple Silicon)

  * Linux




## Guía de instalación de Comfy Desktop (Windows)

Adecuada para **Windows** 10 o posterior. Se recomienda GPU NVIDIA o AMD.

## Guía de instalación de Comfy Desktop (macOS)

Adecuada para macOS con **Apple Silicon**

## Guía de instalación de Comfy Desktop (Linux)

Instala el AppImage o el `.deb`, o compila y ejecuta desde el código fuente.

ComfyUI Portable (Windows)

La versión portable es una versión de ComfyUI que integra un entorno Python integrado independiente; con la versión portable puedes probar las últimas funciones, actualmente solo es compatible con el sistema **Windows**

## Guía de instalación de ComfyUI Portable (Windows)

Compatible con la versión de ComfyUI para **Windows** que se ejecuta en **GPU Nvidia** o **solo con CPU** , siempre usa las últimas confirmaciones (commits) y es completamente portable.

Instalación manual

## Guía de instalación manual de ComfyUI

Compatible con todos los tipos de sistema y de GPU (Nvidia, AMD, Intel, Apple Silicon, Ascend NPU, Cambricon MLU)

## 

​

¿Qué se debe actualizar al actualizar ComfyUI?

Las actualizaciones de ComfyUI consisten principalmente en dos componentes:

  1. Actualizar el código principal de ComfyUI
  2. Actualizar las dependencias principales de ComfyUI, incluidas las dependencias necesarias de Python y los paquetes de dependencias funcionales de ComfyUI

**Código principal** : Nuevos nodos, soporte para nuevos modelos, nuevas funciones, etc. **Dependencias principales** : Incluye principalmente la funcionalidad del frontend de ComfyUI, plantillas de flujo de trabajo, documentación de ayuda de nodos, etc.
    
    
    comfyui-frontend-package   # Funcionalidad del frontend de ComfyUI
    comfyui-workflow-templates # Plantillas de flujo de trabajo de ComfyUI  
    comfyui-embedded-docs      # Documentación de ayuda de nodos de ComfyUI
    comfy-kitchen              # Utilidades principales de ComfyUI
    comfy-aimdo                # Utilidades principales de ComfyUI
    

Estas dependencias principales se mantienen en repositorios separados:

  * [ComfyUI_frontend](https://github.com/Comfy-Org/ComfyUI_frontend/) \- Interfaz del frontend y funciones interactivas
  * [workflow_templates](https://github.com/Comfy-Org/workflow_templates) \- Plantillas de flujo de trabajo prediseñadas
  * [comfyui-embedded-docs](https://github.com/Comfy-Org/embedded-docs) \- Documentación de ayuda de nodos
  * [comfy-kitchen](https://github.com/Comfy-Org/comfy-kitchen) \- Biblioteca de kernels rápida para inferencia de Diffusion con múltiples backends de cómputo
  * [comfy-aimdo](https://github.com/Comfy-Org/comfy-aimdo) \- Asignador de descarga bajo demanda de modelos de IA

Es importante entender la diferencia entre las versiones de desarrollo (nocturnas) y las versiones estables (release):

  * **Versión de desarrollo (nocturna)** : Código del último commit, que te da acceso a las funciones más recientes, pero puede contener posibles problemas
  * **Versión estable (release)** : Basada en lanzamientos estables, normalmente va por detrás de las versiones de desarrollo, pero ofrece mayor estabilidad. Damos soporte a las versiones estables después de que las funciones se prueban y estabilizan

Muchos usuarios suelen encontrarse en versiones estables (release) o versiones de escritorio durante las actualizaciones, pero descubren que las funciones que necesitan solo están disponibles en las versiones de desarrollo. En esos casos, verifica si tu archivo local `ComfyUI/requirements.txt` coincide con las [dependencias de la versión nocturna](https://github.com/Comfy-Org/ComfyUI/blob/master/requirements.txt) para determinar si todas las dependencias admiten las funciones más recientes.

## 

​

Problemas comunes de actualización

### 

​

Frontend, plantillas de flujos de trabajo o nodos faltantes o desactualizados después de las actualizaciones

  * Dependencias no actualizadas correctamente

  * Fallos de actualización de dependencias




Muchos usuarios solo usan el comando `git pull` para actualizar el código de ComfyUI, pero **descuidan la actualización de las dependencias principales** , lo que provoca los siguientes problemas:

  * Funcionalidad del frontend faltante o anómala
  * No se encuentran las plantillas de flujo de trabajo recién agregadas
  * Documentación de ayuda de los nodos desactualizada o faltante
  * Las nuevas funciones carecen del soporte correspondiente en el frontend

Después de usar el comando `git pull`, usa el entorno de ComfyUI correspondiente para ejecutar `pip install -r requirements.txt` y actualizar las dependencias.

Si fallan las actualizaciones de dependencias, suele deberse a problemas de red o de permisos del equipo. Cuando se producen fallos en las dependencias principales durante las actualizaciones, el sistema recurre a versiones anteriores. Normalmente verás registros como este durante el inicio:
    
    
    Falling back to the default frontend.
    ComfyUI frontend version: xxx
    

Sigue estos pasos para solucionar problemas:

  1. Usa `pip list` en el entorno adecuado para ver los paquetes de dependencias instalados actualmente. Si encuentras inconsistencias de versión, usa `pip install -r requirements.txt` en el entorno de ComfyUI para intentar actualizar las dependencias de nuevo.
  2. Si los problemas persisten después de actualizar, revisa tu conexión de red. Los usuarios en China continental pueden necesitar configurar un proxy para acceder de forma fiable a los repositorios de GitHub.
  3. Si los problemas continúan, revisa los permisos del equipo. Si se requieren privilegios de administrador, ejecuta la línea de comandos con derechos de administrador.



### 

​

Cómo actualizar correctamente las dependencias principales

  * Portable

  * Instalación manual

  * Desktop




**Método recomendado** : Usa el script de lote `ComfyUI_windows_portable\update\update_comfyui.bat`, que actualizará tanto el código de ComfyUI como todas las dependencias de Python.**Actualización manual de dependencias** : Si necesitas actualizar las dependencias manualmente, usa el siguiente comando:
    
    
    # Abre la línea de comandos en el directorio de la versión portable
    .\python_embeded\python.exe -m pip install -r ComfyUI\requirements.txt
    

1

Activa el entorno de Python

Si usas Conda para administrar entornos de Python, activa tu entorno primero:
    
    
    conda activate comfyui  # o el nombre de otro entorno
    

2

Actualiza el código

Navega al directorio raíz de ComfyUI y actualiza el código con Git:
    
    
    cd <ComfyUI_ROOT_PATH>
    git pull
    

3

Actualiza las dependencias

Actualiza las dependencias de ComfyUI. Este paso es crucial, especialmente para el `comfyui-frontend-package`:
    
    
    pip install -r requirements.txt
    

La versión Desktop normalmente gestiona las actualizaciones de dependencias de forma automática. Si tienes problemas:

  1. **Verifica si la actualización automática** está habilitada
  2. **Activa la actualización manualmente** : Menú → Ayuda → Buscar actualizaciones
  3. **Reinstala la versión Desktop** (en casos extremos)



### 

​

Solución de problemas de actualización de dependencias principales

Si fallan las actualizaciones de las dependencias principales, sigue estos pasos para solucionar problemas:

1

Comprobar la conexión de red

Si te encuentras en China continental, asegúrate de poder acceder a PyPI o configura un espejo nacional:
    
    
    # Usando el espejo de la Universidad de Tsinghua
    pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
    

2

Instalar los paquetes principales individualmente

Si falla la instalación por lotes, intenta instalar los paquetes individualmente. **Primero revisa los requisitos de versión en`ComfyUI/requirements.txt`**:**Luego instala según las versiones especificadas (usa los números de versión de tu requirements.txt):**
    
    
     pip install comfyui-frontend-package==<version> 
    pip install comfyui-workflow-templates==<version>
    pip install comfyui-embedded-docs==<version>
    pip install comfy-kitchen==<version>
    pip install comfy-aimdo==<version>
    

Se recomienda usar los números de versión exactos especificados en `ComfyUI/requirements.txt`. No actualices a las últimas versiones por tu cuenta, ya que esto puede causar problemas de compatibilidad.

### 

​

¿Por qué no encuentro las nuevas funciones después de actualizar?

Este es uno de los problemas más comunes:

  * Si usas la **versión de escritorio** , es posible que las funciones estén retrasadas porque la versión de escritorio se basa en versiones estables
  * Asegúrate de usar la **versión de desarrollo (nocturna)** , no la **versión estable (release)**

Además, asegúrate de que las dependencias correspondientes se hayan actualizado correctamente durante el proceso de actualización. Si los problemas persisten después de actualizar, consulta la sección Solución de problemas de actualización de dependencias para diagnosticar los problemas.

### 

​

¿Cómo cambiar entre la versión de desarrollo (nocturna) y la versión estable (release)?

Diferencias entre versiones:

  * Versión de desarrollo (nocturna)

  * Versión estable (release)




  * **Características** : contiene el código del commit más reciente
  * **Ventajas** : experimenta primero las últimas funciones y mejoras
  * **Riesgos** : puede contener errores no descubiertos o factores de inestabilidad
  * **Adecuada para** : desarrolladores, testadores y usuarios que quieran experimentar las últimas funciones



  * **Características** : código estable probado y verificado
  * **Ventajas** : alta estabilidad, adecuada para entornos de producción
  * **Desventajas** : las actualizaciones de funciones tienen retrasos y pueden ir por detrás de las versiones de desarrollo durante semanas o meses
  * **Adecuada para** : usuarios que requieren estabilidad y usuarios de entornos de producción



  * Portátil

  * Instalación manual

  * Escritorio




Usa `update_comfyui.bat` en lugar de `update_comfyui_stable.bat`:
    
    
    # Versión de desarrollo (últimas funciones)
    double-click: update_comfyui.bat
    
    # Versión estable
    double-click: update_comfyui_stable.bat
    
    
    
    # Cambiar a la versión de desarrollo
    git checkout master
    git pull
    
    # Cambiar a la última versión estable
    git fetch --tags
    git checkout $(git describe --tags `git rev-list --tags --max-count=1`)
    

La versión de escritorio normalmente se basa en versiones estables y actualmente no admite el cambio de versión. Si necesitas las últimas funciones, te recomendamos:

  1. Esperar a que se actualice la versión de escritorio
  2. O usar la instalación portátil/manual para experimentar las últimas funciones



### 

​

¿Qué hacer cuando ocurren errores después de actualizar?

  1. **Revisa las dependencias** : ejecuta `pip install -r requirements.txt` para asegurarte de que todas las dependencias estén actualizadas
  2. **Revisa los nodos personalizados** : algunos nodos personalizados pueden ser incompatibles con las nuevas versiones
  3. **Revierte la versión** : si los problemas son graves, puedes volver a una versión estable anterior

Si se producen problemas, consulta nuestra página de solución de problemas para encontrar soluciones.

## Solución de problemas

Aprende a solucionar problemas de ComfyUI

### 

​

¿Cómo estar al día con las nuevas funciones?

  * **GitHub Releases** : consulta [ComfyUI Releases](https://github.com/Comfy-Org/ComfyUI/releases) para ver las actualizaciones de la versión estable
  * **Commits de GitHub** : consulta los [últimos commits](https://github.com/Comfy-Org/ComfyUI/commits/master) para entender el progreso del desarrollo
  * **Discusión de la comunidad** : sigue nuestro [blog](https://blog.comfy.org) y [Twitter](https://x.com/comfyui) para conocer las últimas novedades



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/installation/update_comfyui.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/installation/update_comfyui)

[Manual (local)](https://docs.comfy.org/es/installation/manual_install)[Nodos personalizados](https://docs.comfy.org/es/installation/install_custom_node)
