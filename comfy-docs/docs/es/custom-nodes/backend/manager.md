---
url: https://docs.comfy.org/es/custom-nodes/backend/manager/
title: Publicar un nodo personalizado en ComfyUI Manager - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-16T16:52:08.069059+00:00
---

# Publicar un nodo personalizado en ComfyUI Manager - ComfyUI

> Source: https://docs.comfy.org/es/custom-nodes/backend/manager/

## En esta página

Volver arriba

  * Usar ComfyUI Manager
  * Archivos de ComfyUI Manager



Package & Publish

# Publicar un nodo personalizado en ComfyUI Manager

Copiar páginaCopiar página

Registra un nodo personalizado en ComfyUI Manager con una pull request que lo añade a custom-node-list.json, además de los requisitos de repositorio git.

Copiar páginaCopiar página

### Usar ComfyUI Manager

Para que tu nodo personalizado esté disponible a través de **ComfyUI Manager** , debes guardarlo como un repositorio Git (generalmente en `github.com`) y luego enviar un Pull Request en el repositorio Git de **ComfyUI Manager** , en el que hayas editado `custom-node-list.json` para agregar tu nodo. [Más detalles](https://github.com/Comfy-Org/ComfyUI-Manager?tab=readme-ov-file#how-to-register-your-custom-node-into-comfyui-manager). Cuando un usuario instala el nodo, **ComfyUI Manager** hará lo siguiente:

1

Clonar el repositorio

clona el repositorio,

2

Instalar dependencias de Python

instala las dependencias de pip que se enumeran en el repositorio del nodo personalizado en `requirements.txt` (si existe),
    
    
    pip install -r requirements.txt
    

Como siempre ocurre con `pip`, es posible que los requisitos de tu nodo entren en conflicto con los de otros nodos personalizados. No hagas que tu `requirements.txt` sea más restrictivo de lo necesario.

3

Ejecutar script de instalación

ejecuta `install.py`, si existe en el repositorio del nodo personalizado. 

`install.py` se ejecuta desde la ruta raíz del nodo personalizado

### Archivos de ComfyUI Manager

Como se indicó antes, hay varios archivos y scripts que **ComfyUI Manager** usa para administrar el ciclo de vida de un nodo personalizado. Todos son opcionales.

  * `requirements.txt`: dependencias de Python como se mencionó antes
  * `install.py`, `uninstall.py`: se ejecutan cuando instalas o desinstalas el nodo personalizado 

Los usuarios pueden simplemente eliminar el directorio, así que no puedes contar con que `uninstall.py` se ejecute

  * `disable.py`, `enable.py`: hooks opcionales. Solo el flujo antiguo de git-clone los ejecuta al deshabilitar o volver a habilitar un nodo. Las acciones actuales de deshabilitar y habilitar solo mueven la carpeta, así que no dependas de estos scripts 

`enable.py` solo se ejecuta cuando se vuelve a habilitar un nodo deshabilitado; solo debe revertir cualquier cambio hecho en `disable.py`

Al deshabilitar un nodo personalizado, su carpeta se mueve a `ComfyUI/custom_nodes/.disabled/`, y Comfy ignora el módulo mientras está ahí

  * `node_list.json`: solo se requiere si el patrón de `NODE_CLASS_MAPPINGS` de los nodos personalizados no es convencional.

Consulta la [guía de ComfyUI Manager](https://github.com/Comfy-Org/ComfyUI-Manager?tab=readme-ov-file#custom-node-support-guide) para ver los detalles oficiales.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/custom-nodes/backend/manager.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/custom-nodes/backend/manager)

[Publicar nodos](https://docs.comfy.org/es/registry/publishing)[Reclamar nodo](https://docs.comfy.org/es/registry/claim-my-node)
