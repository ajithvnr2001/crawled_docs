---
url: https://docs.comfy.org/es/registry/publishing/
title: Publicar nodos - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:38.741501+00:00
---

# Publicar nodos - ComfyUI

> Source: https://docs.comfy.org/es/registry/publishing/

## En esta página

Volver arriba

  * Configurar una cuenta del registro
    * Ver un tutorial
    * Crear un editor
    * Crear una clave API para publicar en el registro
    * Agregar metadatos
    * Excluir archivos con .comfyignore
  * Publicar en el registro
    * Opción 1: Comfy CLI
    * Opción 2: GitHub Actions



Package & Publish

# Publicar nodos

Copiar páginaCopiar página

Aprende a crear una cuenta de Comfy Registry, un editor, una clave API y metadatos, y a publicar nodos personalizados con Comfy CLI o GitHub Actions.

Copiar páginaCopiar página

## 

​

Configurar una cuenta del registro

Sigue los pasos a continuación para configurar una cuenta del registro y publicar tu primer nodo.

### 

​

Ver un tutorial

### 

​

Crear un editor

Un editor es una identidad que puede publicar nodos personalizados en el registro. Cada nodo personalizado debe incluir un identificador de editor en el [archivo](https://docs.comfy.org) pyproject.toml. Ve a [Comfy Registry](https://registry.comfy.org) y crea una cuenta de editor. Tu ID de editor es único a nivel global y no podrás cambiarlo más tarde porque se usa en la URL de tu nodo personalizado. Encontrarás tu ID de editor después del símbolo `@` en tu página de perfil. ![Hero oscuro](https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/publisherid.png?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=95e3271276938f1ec1226f172ffc020f)

### 

​

Crear una clave API para publicar en el registro

**Importante:** Esta clave API sirve específicamente para **publicar nodos personalizados en el registro y ComfyUI-Manager**. Si lo que buscas es usar Nodos asociados de pago en tus flujos de trabajo, consulta [Descripción general de los Nodos asociados](https://docs.comfy.org/es/tutorials/partner-nodes/overview).

Ve [aquí](https://registry.comfy.org/nodes) y haz clic en el editor para el que quieres crear una clave API. Esta clave se usará para publicar nodos personalizados en el registro (que impulsa ComfyUI-Manager) mediante la CLI o GitHub Actions. ![Crear clave para un editor específico](https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/pat-1.png?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=6f9c94583f78457419cfde793f49f387) Asigna un nombre a la clave API y guárdala en un lugar seguro. Si la pierdes, tendrás que crear una clave nueva. ![Crear clave API](https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/pat-2.png?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=490347389e83b978f4c65b0e6a7b5d33)

### 

​

Agregar metadatos

¿Ya instalaste comfy-cli? [Hazlo primero](https://docs.comfy.org/es/comfy-cli/getting-started).
    
    
    comfy node init
    

Este comando generará los siguientes metadatos:
    
    
    # pyproject.toml
    [project]
    name = "" # Identificador único para tu nodo. Inmutable después de la creación.
    description = ""
    version = "1.0.0" # Versión del nodo personalizado. Debe usar versionado semántico.
    license = { file = "LICENSE.txt" }
    dependencies  = [] # Se completa desde requirements.txt
    
    [project.urls]
    Repository = "https://github.com/..."
    
    [tool.comfy]
    PublisherId = "" # TODO (completa el ID de editor desde el sitio web de Comfy Registry).
    DisplayName = "" # Nombre para mostrar del nodo personalizado. Puedes cambiarlo más tarde.
    Icon = "https://example.com/icon.png" # SVG, PNG, JPG o GIF (MÁX. 800x400px)
    

Agrega este archivo a tu repositorio. Consulta las [especificaciones](https://docs.comfy.org/es/registry/specifications) para obtener más información sobre el archivo pyproject.toml.

### 

​

Excluir archivos con `.comfyignore`

De forma predeterminada, `comfy node publish` empaqueta todos los archivos rastreados por `git`. Para mantener fuera del archivo publicado los archivos solo para desarrollo (pruebas, recursos de diseño, muestras grandes), agrega un archivo `.comfyignore` en la raíz de tu repositorio. La sintaxis coincide con la de [`.gitignore`](https://git-scm.com/docs/gitignore):
    
    
    # Recursos solo para desarrollo
    docs/
    tests/
    *.psd
    .vscode/
    

  * `.comfyignore` se aplica sobre `.gitignore`: los archivos que git no rastrea ya están excluidos. Usa `.comfyignore` para descartar archivos que _conservas_ en git pero que no quieres en el archivo del registro.
  * Los directorios listados en [`[tool.comfy].includes`](https://docs.comfy.org/es/registry/specifications) se incluyen de forma forzada aunque coincidan con un patrón de `.comfyignore` (útil cuando una carpeta `dist/` compilada está ignorada por git pero debe incluirse en el paquete).
  * Haz commit de `.comfyignore` en tu repositorio para que las ejecuciones locales y CI generen el mismo archivo.



## 

​

Publicar en el registro

### 

​

Opción 1: Comfy CLI

Ejecuta el comando de abajo para publicar tu nodo manualmente en el registro.
    
    
    comfy node publish
    

Se te pedirá la clave API.
    
    
    API Key for publisher '<publisher id>': ****************************************************
    
    ...Version 1.0.0 Published. 
    See it here: https://registry.comfy.org/publisherId/your-node
    

Ten en cuenta que la clave API está oculta de forma predeterminada.

Al copiar y pegar con CTRL+V (en Windows), es posible que tu clave API tenga un \x16 adicional al final, por ejemplo: ************************************************\x16.Se recomienda copiar y pegar tu clave API haciendo clic con el botón derecho.

### 

​

Opción 2: GitHub Actions

Publica tu nodo automáticamente mediante GitHub Actions.

1

Configurar un secreto de GitHub

Ve a Configuraciones -> Secretos y variables -> Acciones -> En la pestaña Secretos, en Secretos del repositorio -> Nuevo secreto del repositorio.Crea un secreto llamado `REGISTRY_ACCESS_TOKEN` y guarda tu clave API como valor.

2

Crear una acción de GitHub

Copia el código de abajo y pégalo aquí `/.github/workflows/publish_action.yml`
    
    
    name: Publish to Comfy registry
    on:
      workflow_dispatch:
      push:
        branches:
          - main
        paths:
          - "pyproject.toml"
    
    jobs:
      publish-node:
        name: Publish Custom Node to registry
        runs-on: ubuntu-latest
        steps:
          - name: Check out code
            uses: actions/checkout@v7
          - name: Publish Custom Node
            uses: Comfy-Org/publish-node-action@main
            with:
              personal_access_token: ${{ secrets.REGISTRY_ACCESS_TOKEN }} ## Agrega tu propio token de acceso personal a los secretos de tu repositorio de GitHub y haz referencia a él aquí.
    

Si tu rama de trabajo tiene otro nombre además de `main`, como `master`, agrega el nombre en la sección branches.

3

Probar la acción de GitHub

Envía una actualización al número de versión de tu `pyproject.toml`. Deberías ver tu nodo actualizado en el registro.

La acción de GitHub se ejecutará automáticamente cada vez que envíes una actualización a tu archivo `pyproject.toml`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/registry/publishing.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/registry/publishing)

[Descripción general del Registry](https://docs.comfy.org/es/registry/overview)[Reclamar mi nodo](https://docs.comfy.org/es/registry/claim-my-node)
