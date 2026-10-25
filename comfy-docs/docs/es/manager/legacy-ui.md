---
url: https://docs.comfy.org/es/manager/legacy-ui/
title: Administrar nodos personalizados con ComfyUI-Manager (interfaz cl\u00e1sica) - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-25T12:24:49.153227+00:00
---

# Administrar nodos personalizados con ComfyUI-Manager (interfaz clásica) - ComfyUI

> Source: https://docs.comfy.org/es/manager/legacy-ui/

## En esta página

  * Gestión de nodos personalizados de ComfyUI
    * Instalar nodos
    * Instalar nodos faltantes
    * Actualizar nodos
    * Desinstalar nodos
  * Administrador de instantáneas



Gestión de nodos

# Administrar nodos personalizados con ComfyUI-Manager (interfaz clásica)

Copiar páginaCopiar página

Instala, actualiza y administra nodos personalizados con ComfyUI-Manager usando la interfaz clásica

Copiar páginaCopiar página

## 

​

Gestión de nodos personalizados de ComfyUI

Aprende a instalar nodos personalizados a través de ComfyUI Manager

### 

​

Instalar nodos

1

Haz clic en el botón Administrador de la interfaz de ComfyUI

Haz clic en el botón **Administrador** del menú principal (barra superior).![Botón Administrador](https://mintcdn.com/dripart/H4QqpI0-Odea2uWk/images/manager/manager_button.jpg?fit=max&auto=format&n=H4QqpI0-Odea2uWk&q=85&s=e93af1b2171591cc6713a5dabdb4ea6a)

2

Selecciona Instalar nodos

![Entrada del Administrador](https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/manager_entry.jpg?fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=a278016fa7a36ed7ea6d2911c98fa0cc)

3

Explora o busca el nodo que quieres instalar

![Lista del Administrador](https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/manager_list.jpg?fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=4dd474636f9f44bc951ee7acb69055d9)

4

Haz clic en **Instalar** para instalar el nodo

![Diálogo de instalación de nodos](https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/manager_install_node.jpg?fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=b70fd2859daa7effb3f82dc29565c0cc)

  1. Prefiere la **última** versión si está disponible
  2. Haz clic en **Seleccionar** para instalar el nodo



  * Los números de versión con dígitos son versiones publicadas por los autores en el [registro](https://registry.comfy.org/), equivalentes a versiones estables
  * La versión nocturna es la última versión que los autores actualizan en GitHub, equivale a la versión de desarrollo; por lo general no pasa por un escaneo de seguridad y tiene factores de inestabilidad

La configuración de seguridad predeterminada de ComfyUI no permite la instalación directa de versiones **nocturnas**. Puedes consultar la [Política de seguridad](https://docs.comfy.org/es/manager/troubleshooting#pol%C3%ADtica-de-seguridad) para más detalles

5

Espera a que finalice la instalación de las dependencias y luego reinicia ComfyUI

Después de hacer clic en instalar, el Administrador completará automáticamente la instalación de las dependencias y te pedirá que reinicies ComfyUI cuando la instalación haya finalizado![Reinicia ComfyUI y actualiza el navegador después de la instalación](https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-manager-7.jpg?fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=0d0a41967984241d0cd9f91718142abc)![Reinicia ComfyUI y actualiza el navegador después de la instalación](https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-manager-8.jpg?fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=4fabdae56e5d3dc110b9bc69a0dc78f8)

6

Verifica si el complemento se instaló correctamente

Después de reiniciar, verifica en ComfyUI Manager si el complemento correspondiente se instaló correctamente y si hay mensajes de error `import failed`![Verifica si el complemento se instaló correctamente](https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-manager-9.jpg?fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=c1d9fa38bbfe862ae661177e2948599c)

### 

​

Instalar nodos faltantes

Los nodos faltantes son una situación común al cargar flujos de trabajo. Por lo general, hay dos tipos de nodos faltantes:

  1. Falta un nodo principal: la versión de ComfyUI no es la última; consulta [Actualizar ComfyUI](https://docs.comfy.org/es/installation/update_comfyui) para actualizar ComfyUI
  2. Faltan nodos personalizados: faltan nodos personalizados de terceros; puedes consultar esta guía para instalarlos

Una vez instalado ComfyUI-Manager, si faltan nodos personalizados al importar flujos de trabajo, se te avisará con la información de los nodos faltantes ![Aviso de nodos faltantes](https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/manger_missing_nodes-1.jpg?fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=276f807577062ba0cd5017a20d2f1e69)

  1. Haz clic en **Abrir administrador** para activar la opción correspondiente

![Aviso de nodos faltantes](https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/manger_missing_nodes-2.jpg?fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=4913285ef58667257877dbc51f308334) 2\. Haz clic en **Install Missing Custom Nodes** (Instalar nodos personalizados faltantes) en el menú del Manager para entrar a la interfaz de la lista de nodos faltantes ![Aviso de nodos faltantes](https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/manger_missing_nodes-3.jpg?fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=6b95d711cbbb211de0d9025b4fe75eba) 3\. Consulta e instala los nodos correspondientes en la lista de nodos

Si notas que la lista de nodos faltantes no encuentra el nodo correspondiente, por lo general se debe a varias situaciones:

  1. El autor del nodo no ha enviado ni registrado el nodo personalizado en el [registro](https://docs.comfy.org/registry/overview)
  2. El nodo correspondiente no es de código abierto; puede ser un nodo restringido de ciertos autores o de plataformas limitadas
  3. El autor original cambió la versión y eliminó el nodo correspondiente



### 

​

Actualizar nodos

![Versión del nodo](https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/manger_node_version.jpg?fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=cd663ba4db2aa4477a2784935317b8e8)

  1. Cambia el filtro a **Actualizar** para filtrar los nodos que se pueden actualizar en la lista actual de nodos
  2. Haz clic en el botón **Actualizar** para actualizar el nodo



### 

​

Desinstalar nodos

![Desinstalar nodos](https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/manger_remove_nodes.jpg?fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=5bbc0ba5314820111faa0d366cedeafc)

  1. Selecciona el filtro “Instalado” en la lista de nodos para filtrar los nodos instalados en la lista actual de nodos
  2. Haz clic derecho en el nodo correspondiente y selecciona **Desinstalar** para desinstalarlo



> Desinstalar el nodo correspondiente no eliminará la instalación de las dependencias asociadas

Para conocer otros métodos de instalación de complementos, consulta el siguiente artículo

## Instalar nodos personalizados

Aprende a instalar nodos personalizados manualmente

## 

​

Administrador de instantáneas

Las instantáneas guardan el estado actual de tu instalación, lo que te permite restaurar a un estado anterior. ![Administrador de instantáneas](https://raw.githubusercontent.com/ltdrdata/ComfyUI-extension-tutorials/Main/ComfyUI-Manager/images/snapshot.jpg) Las instantáneas se guardan automáticamente cuando haces clic en **Guardar instantánea** o usas **Actualizar Todos**. Los archivos de instantáneas se almacenan en: `<USER_DIRECTORY>/default/ComfyUI-Manager/snapshots` Para restaurar: abre el Administrador de Instantáneas, selecciona una instantánea y haz clic en **Restaurar**.

La restauración surte efecto en el próximo inicio de ComfyUI. Para los Nodos Personalizados que no son gestionados por Git, el soporte de instantáneas es incompleto.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/manager/legacy-ui.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/manager/legacy-ui)

[Nueva interfaz](https://docs.comfy.org/es/manager/pack-management)[Config](https://docs.comfy.org/es/manager/configuration)
