---
url: https://docs.comfy.org/es/development/deploy/cloud/
title: Inicio r\u00e1pido de Comfy Cloud - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:27.237136+00:00
---

# Inicio rápido de Comfy Cloud - ComfyUI

> Source: https://docs.comfy.org/es/development/deploy/cloud/

## En esta página

Volver arriba

  * Inicio rápido
  * Próximos pasos



Comfy Cloud

# Inicio rápido de Comfy Cloud

Copiar páginaCopiar página

Ejecuta un flujo de trabajo en formato API en Comfy Cloud con una suscripción de pago, una clave API y el SDK de Comfy.

Copiar páginaCopiar página

Comfy Cloud es un entorno de ComfyUI totalmente administrado y siempre disponible. Crea flujos de trabajo en el navegador o ejecútalos mediante el SDK. No hay ningún Build ni despliegue que crear.

¿Es tu primera vez con Comfy Cloud? Empieza con la [introducción a Comfy Cloud](https://docs.comfy.org/es/get_started/cloud). Este inicio rápido muestra cómo ejecutar flujos de trabajo desde una aplicación.

## 

​

Inicio rápido

Requiere una suscripción de pago, una [clave API](https://docs.comfy.org/es/development/api-development/getting-an-api-key) y un flujo de trabajo en formato API. Los [SDK de Comfy](https://docs.comfy.org/es/development/api-development/sdks) apuntan a Cloud de forma predeterminada.

1

Crear una clave API

Crea una clave API en [platform.comfy.org](https://platform.comfy.org). Consulta [Obtener una clave API](https://docs.comfy.org/es/development/api-development/getting-an-api-key) para más detalles.

2

Instalar el SDK

Python

TypeScript
    
    
    pip install comfy-sdk
    
    
    
    npm i @comfyorg/sdk
    

3

Exportar un flujo de trabajo en formato API

En el editor de Cloud, guarda tu flujo de trabajo ya probado como `workflow_api.json` con `File → Export Workflow (API)`. Consulta [Formato API de flujo de trabajo](https://docs.comfy.org/es/development/api-development/workflow-api-format).

4

Ejecutarlo

Python

TypeScript
    
    
    from comfy_sdk import Comfy
    
    client = Comfy(api_key="comfyui-...")  # Comfy Cloud es el objetivo predeterminado
    
    wf = client.workflows.from_file("workflow_api.json")
    
    job = client.run(wf)
    for output in job.get_outputs("9"):
        output.to_file(output.name)
    
    
    
    import { Comfy } from "@comfyorg/sdk";
    
    const client = new Comfy({ apiKey: "comfyui-..." }); // Comfy Cloud es el objetivo predeterminado
    
    const wf = await client.workflows.fromFile("workflow_api.json");
    
    const job = await client.run(wf);
    await job.getOutputs("9")[0].toFile("out.png");
    

`"9"` es el ID del nodo de salida. Consulta la [guía del SDK](https://docs.comfy.org/es/development/api-development/sdks) para las entradas, el progreso y el manejo de errores.

El mismo código del SDK puede apuntar a [despliegues de Comfy API](https://docs.comfy.org/es/development/serverless/quickstart) y a [ComfyUI autoalojado](https://docs.comfy.org/es/development/deploy/self-hosting). Consulta [Ejecutar flujos de trabajo](https://docs.comfy.org/es/development/run-workflows/overview).

## 

​

Próximos pasos

## Uso y límites

Consulta cómo funcionan los créditos de Cloud y las tareas simultáneas.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/deploy/cloud.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/deploy/cloud)

[Guía de despliegue](https://docs.comfy.org/es/development/serverless/overview)[Uso y límites](https://docs.comfy.org/es/development/deploy/cloud-usage)
