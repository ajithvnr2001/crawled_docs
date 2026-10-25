---
url: https://docs.comfy.org/es/manager/pack-management/
title: Nodos personalizados (nueva interfaz) - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-25T12:24:49.491526+00:00
---

# Nodos personalizados (nueva interfaz) - ComfyUI

> Source: https://docs.comfy.org/es/manager/pack-management/

## En esta página

  * Descripción general de la nueva interfaz
  * Gestión de nodos
    * Buscar nodos
    * Instalar nodos
    * Actualizar nodos
    * Encontrar nodos faltantes
    * Desinstalar nodos
  * Preguntas frecuentes



Gestión de nodos

# Nodos personalizados (nueva interfaz)

Copiar páginaCopiar página

Instala, actualiza y administra nodos personalizados con ComfyUI-Manager usando la nueva interfaz

Copiar páginaCopiar página

Si no estás usando la nueva interfaz, consulta la sección [Cambiar entre la nueva interfaz y la clásica](https://docs.comfy.org/es/manager/install) para aprender a cambiar.

## 

​

Descripción general de la nueva interfaz

![Nueva interfaz](https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_labeled.jpg?fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=b169a5dbcb0607bf29e499278a901dc2)

  1. **Barra lateral izquierda (Filtros)** : Filtra nodos instalados, nodos en el flujo de trabajo, nodos faltantes, nodos actualizables, etc.
  2. **Barra de búsqueda superior** : Busca paquetes de nodos (Node Pack) o nodos individuales (Node); cambia el tipo de búsqueda con el menú desplegable Filtrar
  3. **Panel de detalles derecho** : Haz clic en un nodo para mostrar información detallada, incluida la descripción, el estado de habilitación, la información de versión, etc. La pestaña Descripción contiene la información del repositorio y la pestaña Nodes muestra una vista previa de todos los nodos



## 

​

Gestión de nodos

Aprende a usar el nuevo ComfyUI Manager para administrar nodos personalizados

### 

​

Buscar nodos

![Filtrar](https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_filter.jpg?fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=39b734a9514bce3d14ec83ff053f2c99) El Administrador permite buscar paquetes de nodos y nodos individuales por separado. Como se muestra arriba, puedes cambiar el tipo de búsqueda alternando el filtro.

  * Node Pack: Un paquete de nodos personalizados completo
  * Individual Node: Busca nodos individuales dentro de los paquetes de nodos



### 

​

Instalar nodos

![Instalar nodos](https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_install_pack.jpg?fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=7968ebd2eb538909882c4b2f2efdf83d)

  1. Selecciona la tarjeta del nodo correspondiente
  2. Haz clic en **Install** en la información del nodo expandida
  3. O selecciona una versión específica en **Version** para instalar



### 

​

Actualizar nodos

En el filtro **Update available** , puedes filtrar los nodos que tienen actualizaciones disponibles en la lista de nodos actual ![Actualizar nodos](https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_update_pack.jpg?fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=439f256ae789bbfee69e81ff0a87dfb9)

  1. Los nodos actualizables mostrarán un indicador de flecha de actualización
  2. Selecciona una versión específica en **Version**
  3. Haz clic en el botón **Update** después de seleccionar una versión para actualizar



### 

​

Encontrar nodos faltantes

![Encontrar nodos faltantes](https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_missing_packs_prompt.jpg?fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=48daeed1ac09b0f725dc311be5c60871) Si tu ComfyUI Manager está instalado correctamente, aparecerá un aviso al cargar un flujo de trabajo con nodos faltantes

  1. Puedes elegir **Install All** para instalar todos los nodos a la vez
  2. O elegir **Open Manager** para abrir el Manager y revisar los detalles antes de instalar

![Encontrar nodos faltantes](https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_missing_pack.jpg?fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=c800b0999e45d8f3f45ceead054a9dbc) Para encontrar nodos faltantes en un flujo de trabajo, selecciona el nodo correspondiente y luego haz clic en el botón **Missing** en el panel de vista previa para encontrar los nodos faltantes

### 

​

Desinstalar nodos

![Desinstalar nodos](https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_uninstall_pack.jpg?fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=f40ab0c5454f6646566c887db41d2559) Para desinstalar un nodo instalado, selecciona el nodo correspondiente y luego haz clic en el botón **Uninstall** en el panel de vista previa para desinstalarlo

## 

​

Preguntas frecuentes

  1. ¿Por qué no encuentro el nodo que necesito? El nuevo Administrador solo permite instalar nodos desde el [registro](https://docs.comfy.org/registry/overview). Si tu nodo no está registrado en el registro, regístralo primero en el Administrador.
  2. ¿Por qué no encuentro la opción de instalar mediante git? Por seguridad y estabilidad del sistema de usuarios de ComfyUI, la nueva interfaz no permite instalar nodos mediante git. Consulta [Instalar nodos personalizados manualmente](https://docs.comfy.org/es/installation/install_custom_node) para aprender a instalar nodos personalizados manualmente.



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/manager/pack-management.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/manager/pack-management)

[Instalar](https://docs.comfy.org/es/manager/install)[Interfaz clásica](https://docs.comfy.org/es/manager/legacy-ui)
