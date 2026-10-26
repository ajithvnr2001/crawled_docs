---
url: https://docs.comfy.org/es/development/serverless/quickstart/
title: Inicio r\u00e1pido de Comfy API - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:27.998599+00:00
---

# Inicio rápido de Comfy API - ComfyUI

> Source: https://docs.comfy.org/es/development/serverless/quickstart/

## En esta página

Volver arriba

  * Empezar con un agente (recomendado)
  * Inicio rápido
  * Otras formas de empezar
  * Próximos pasos



API de Comfy

# Inicio rápido de Comfy API

Copiar páginaCopiar página

Usa un agente de IA y comfy-cli para compilar, publicar y desplegar un entorno local de ComfyUI como endpoint gestionado.

Copiar páginaCopiar página

## 

​

Empezar con un agente (recomendado)

Inicia tu agente de programación en la carpeta de la instalación local de ComfyUI que quieres desplegar. Pega este prompt:
    
    
    Install or update comfy-cli, then read its Build and Deploy skills:
    
    pip install -U comfy-cli
    comfy skills show comfy-build
    comfy skills show comfy-deploy
    
    Use comfy-build to inspect this local ComfyUI install and package its models, custom nodes, and pinned dependencies into a Comfy API Build. Show me what will be included and create a Linux/NVIDIA release. Then use comfy-deploy to show the available GPU and region options, worker bounds, and current rates. Wait for my approval before creating a deployment. After approval, deploy it and explain how to run a workflow.
    

## 

​

Inicio rápido

Usa estos comandos cuando la instalación local y un [flujo de trabajo en formato API](https://docs.comfy.org/es/development/api-development/workflow-api-format) guardado como `workflow_api.json` estén listos.

1

Inicializar
    
    
    comfy build init --name "my-comfy-build" --models-dir ./models --custom-nodes-dir ./custom_nodes
    

2

Publicar y crear una versión

Sube el Build y sus recursos, consulta los objetivos disponibles y espera a que termine la versión para Linux/NVIDIA:
    
    
    comfy build push
    comfy build refs build-targets
    comfy build release create --target linux/nvidia --watch
    

3

Iniciar un despliegue

Consulta el catálogo para ver los pares de GPU y región disponibles y luego reemplaza los marcadores de GPU, región y límites de workers con tus configuraciones:
    
    
    comfy deploy refs compute
    comfy deploy up --gpu <gpu> --region <region> --min <min-workers> --max <max-workers> --watch
    

4

Ejecutar el flujo de trabajo

Usa el ID de despliegue que imprime `comfy deploy up` con `--deployment`:
    
    
    comfy deploy run \
      --workflow workflow_api.json \
      --deployment <deployment-id> \
      --output-dir ./results
    

## 

​

Otras formas de empezar

Usa estas rutas si tu entorno o tu flujo de trabajo ya existen en Comfy Desktop o en un archivo de flujo de trabajo.

## Instantánea de Comfy Desktop

Exporta una instantánea desde Desktop y luego impórtala en el Build Wizard.

## Importar JSON de flujo de trabajo

Inicia un Build importando un flujo de trabajo guardado en el Build Wizard.

## 

​

Próximos pasos

## Comfy Workflows

Explora los flujos de trabajo de ComfyUI compartidos por la comunidad.

## Aplicaciones

Explora las aplicaciones de la comunidad creadas con ComfyUI.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/serverless/quickstart.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/serverless/quickstart)

[Descripción general](https://docs.comfy.org/es/development/deploy/overview)[Fuentes del Build](https://docs.comfy.org/es/development/serverless/build-sources)
