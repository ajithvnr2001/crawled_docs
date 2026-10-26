---
url: https://docs.comfy.org/es/registry/cicd/
title: CI/CD de nodos personalizados - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:38.481954+00:00
---

# CI/CD de nodos personalizados - ComfyUI

> Source: https://docs.comfy.org/es/registry/cicd/

## En esta página

Volver arriba

  * Introducción
    * Ejecutar flujos de trabajo de Comfy con GitHub Actions
    * Resultados
    * Publicar versiones desde GitHub Actions



Package & Publish

# CI/CD de nodos personalizados

Copiar páginaCopiar página

Prueba nodos personalizados de ComfyUI antes de publicar con Comfy-Action en GitHub Actions y revisa los resultados en el Panel de CI/CD.

Copiar páginaCopiar página

## 

​

Introducción

Cuando haces cambios en nodos personalizados, no es raro romper cosas en Comfy o en otros nodos personalizados. A menudo no es realista probar en todos los sistemas operativos y en distintas configuraciones de Pytorch.

### 

​

Ejecutar flujos de trabajo de Comfy con GitHub Actions

[Comfy-Action](https://github.com/Comfy-Org/comfy-action) te permite ejecutar un archivo workflow.json de Comfy en GitHub Actions. Admite la descarga de modelos y nodos personalizados, y se ejecuta en Linux/Mac/Windows.

### 

​

Resultados

Los archivos de salida se suben al [Panel de CI/CD](https://ci.comfy.org/) y puedes revisarlos como último paso antes de confirmar nuevos cambios o publicar nuevas versiones del nodo personalizado. ![ComfyCI](https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfyci.png?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=443608968123247168b89b026ed2ae0e)

### 

​

Publicar versiones desde GitHub Actions

[Publish Node Action](https://github.com/Comfy-Org/node-publish-action) publica en el Registro la versión indicada en tu `pyproject.toml`, así que basta con aumentar la versión para lanzar una nueva entrega. Agrega tu token de acceso al Registro como secreto del repositorio con el nombre `REGISTRY_ACCESS_TOKEN` en **Settings** > **Secrets and variables** > **Actions** , y luego agrega este flujo de trabajo:
    
    
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
            uses: actions/checkout@v4
          - name: Publish Custom Node
            uses: Comfy-Org/publish-node-action@main
            with:
              personal_access_token: ${{ secrets.REGISTRY_ACCESS_TOKEN }}
    

La versión publicada es el campo `version` de `pyproject.toml`. Actualízalo antes de que se ejecute el flujo de trabajo.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/registry/cicd.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/registry/cicd)

[Estándares de calidad y seguridad](https://docs.comfy.org/es/registry/standards)[pyproject.toml](https://docs.comfy.org/es/registry/specifications)
