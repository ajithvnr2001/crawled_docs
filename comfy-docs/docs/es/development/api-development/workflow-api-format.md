---
url: https://docs.comfy.org/es/development/api-development/workflow-api-format/
title: Formato de API de flujos de trabajo - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:52.475303+00:00
---

# Formato de API de flujos de trabajo - ComfyUI

> Source: https://docs.comfy.org/es/development/api-development/workflow-api-format/

## En esta página

Volver arriba

  * Formato de guardado vs. formato de API
  * Cómo exportar
  * Convertir entre formatos
  * Páginas relacionadas



Ejecutar flujos de trabajo

# Formato de API de flujos de trabajo

Copiar páginaCopiar página

Comprende el formato de API de los flujos de trabajo de ComfyUI y cómo exportarlos

Copiar páginaCopiar página

Los flujos de trabajo de ComfyUI son objetos JSON que describen un gráfico de nodos. Cuando llamas a ComfyUI de forma programática, ya sea a través de la API de Cloud o ejecutando tu propio servidor, el flujo de trabajo debe enviarse en **formato API** , una estructura JSON especializada que difiere del formato de guardado habitual que se usa en el navegador. Esta página explica las diferencias y cómo exportar tus flujos de trabajo correctamente.

* * *

## 

​

Formato de guardado vs. formato de API

El frontend de ComfyUI puede guardar flujos de trabajo en dos formatos:

| Formato de guardado| Formato de API  
---|---|---  
**Menú File**| `File → Save` o `Ctrl+S`| `File → Export Workflow (API)`  
**Extensión de archivo**| `.json`| `.json`  
**Claves de nodo**|  Títulos o etiquetas de nodo| IDs numéricos de nodo  
**Valores de widget**|  Incluidos| Incluidos  
**Datos de posición y disposición**|  Incluidos (x, y, ancho)| **Excluidos**  
**Colores y grupos**|  Incluidos| **Excluidos**  
**Uso**|  Reabrir en el frontend| Envío por API  
**Se puede cargar en la UI**|  Sí| Sí, pero sin la disposición  
  
La diferencia clave: **el formato de API omite los metadatos de la UI** (posiciones, colores, grupos, tamaños de nodo) que solo se necesitan para la edición visual en el frontend. Esto mantiene el JSON más pequeño y limpio para el uso programático.

* * *

## 

​

Cómo exportar

Abre tu flujo de trabajo en el frontend de ComfyUI y luego ve a `File → Export Workflow (API)`:

![Guardando un flujo de trabajo en formato API](https://mintcdn.com/dripart/ozpqEvCuCvE4rrKe/images/development/export_workflow_api_format.png?fit=max&auto=format&n=ozpqEvCuCvE4rrKe&q=85&s=8a8d872f29df9d6a39326899c06714ed)

Exportar un flujo de trabajo en formato API desde el frontend de ComfyUI

Esto descargará un archivo `.json` que contiene solo los datos relevantes para la API:
    
    
    {
      "3": {
        "inputs": {
          "seed": 156680208700286,
          "steps": 20,
          "cfg": 8,
          "sampler_name": "euler",
          "scheduler": "normal",
          "denoise": 1,
          "model": [
            "4",
            0
          ],
          "positive": [
            "6",
            0
          ],
          "negative": [
            "7",
            0
          ],
          "latent_image": [
            "5",
            0
          ]
        },
        "class_type": "KSampler",
        "_meta": {
          "title": "KSampler"
        }
      },
      "4": {
        "inputs": {
          "ckpt_name": "v1-5-pruned-emaonly-fp16.safetensors"
        },
        "class_type": "CheckpointLoaderSimple",
        "_meta": {
          "title": "Load Checkpoint"
        }
      },
      "5": {
        "inputs": {
          "width": 512,
          "height": 512,
          "batch_size": 1
        },
        "class_type": "EmptyLatentImage",
        "_meta": {
          "title": "Empty Latent Image"
        }
      },
      "6": {
        "inputs": {
          "text": "beautiful scenery nature glass bottle landscape, , purple galaxy bottle,",
          "clip": [
            "4",
            1
          ]
        },
        "class_type": "CLIPTextEncode",
        "_meta": {
          "title": "CLIP Text Encode (Prompt)"
        }
      },
      "7": {
        "inputs": {
          "text": "text, watermark",
          "clip": [
            "4",
            1
          ]
        },
        "class_type": "CLIPTextEncode",
        "_meta": {
          "title": "CLIP Text Encode (Prompt)"
        }
      },
      "8": {
        "inputs": {
          "samples": [
            "3",
            0
          ],
          "vae": [
            "4",
            2
          ]
        },
        "class_type": "VAEDecode",
        "_meta": {
          "title": "VAE Decode"
        }
      },
      "9": {
        "inputs": {
          "filename_prefix": "ComfyUI",
          "images": [
            "8",
            0
          ]
        },
        "class_type": "SaveImage",
        "_meta": {
          "title": "Save Image"
        }
      }
    }
    

* * *

## 

​

Convertir entre formatos

Si tienes un flujo de trabajo en formato de guardado y lo necesitas en formato API, el método más sencillo es:

  1. Abre el archivo `.json` usando `File → Load` en la interfaz
  2. Expórtalo con `File → Export Workflow (API)`



* * *

## 

​

Páginas relacionadas

  * [Ejecutar flujos de trabajo](https://docs.comfy.org/es/development/run-workflows/overview): compara las opciones de API y de despliegue
  * [Descripción general de la API de Cloud](https://docs.comfy.org/es/development/cloud/overview): envía flujos de trabajo en formato API a Comfy Cloud
  * [Ejemplos de API](https://docs.comfy.org/es/development/comfyui-server/api-examples): observa flujos de trabajo en formato API en acción
  * [Obtener una clave API](https://docs.comfy.org/es/development/api-development/getting-an-api-key): requerida para la API de Cloud y los Nodos asociados



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/api-development/workflow-api-format.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/api-development/workflow-api-format)

[Proxy de API](https://docs.comfy.org/es/development/comfyui-server/api-proxy)[Metadatos de flujos de trabajo](https://docs.comfy.org/es/development/api-development/workflow-metadata)
