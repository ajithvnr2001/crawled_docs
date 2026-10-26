---
url: https://docs.comfy.org/es/development/deploy/overview/
title: Implementar ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:27.766835+00:00
---

# Implementar ComfyUI - ComfyUI

> Source: https://docs.comfy.org/es/development/deploy/overview/

## En esta página

Volver arriba

  * Implementar desde la aplicación ComfyUI
    * Crea con tu agente
  * Siguiente paso: ejecutar flujos de trabajo contra el despliegue



Desplegar ComfyUI

# Implementar ComfyUI

Copiar páginaCopiar página

Compara Comfy Cloud, las implementaciones gestionadas de la API de Comfy y el autoalojamiento para elegir cómo ejecutar ComfyUI.

Copiar páginaCopiar página

Elige Comfy Cloud para tener un ComfyUI administrado y siempre disponible, Comfy API para un entorno versionado desplegado como endpoint, o autoalojamiento para la infraestructura que administras tú.

## Comfy Cloud

Ejecuta flujos de trabajo sin crear un Build ni un despliegue.

## Comfy API

Empaqueta modelos y nodos personalizados en un endpoint administrado con escalado automático.

## Self-Host

Ejecuta ComfyUI en tu propio hardware, en GPUs alquiladas o en contenedores.

Las tres opciones ejecutan [flujos de trabajo en formato API](https://docs.comfy.org/es/development/api-development/workflow-api-format). Elige según si quieres que Comfy administre el entorno o si prefieres administrarlo tú mismo.

## 

​

Implementar desde la aplicación ComfyUI

ComfyUI agrega una entrada **Implementar en la API de Comfy** al menú **Acciones del flujo de trabajo** de cada flujo de trabajo de nivel superior. Está disponible en la aplicación local, Comfy Cloud y la aplicación Desktop, y la entrada aparece marcada como **NEW** en el menú.

1

Abrir Acciones del flujo de trabajo

En la barra superior, abre el menú **Acciones del flujo de trabajo** en la pestaña del flujo de trabajo.

2

Elegir Implementar en la API de Comfy

ComfyUI activa el flujo de trabajo y luego abre una tarjeta de introducción con un video breve del producto y un resumen de los paquetes de nodos, los modelos y las clases de nodo que usa el flujo de trabajo.

3

Abrir la plataforma

Haz clic en **Implementar en la plataforma** para continuar en [platform.comfy.org](https://platform.comfy.org). El Build Wizard que encontrarás allí parte de un JSON de flujo de trabajo importado o de una instantánea de Comfy Desktop, y [Orígenes de compilación](https://docs.comfy.org/es/development/serverless/build-sources) cubre ambos casos. La tarjeta también incluye un enlace **Leer la documentación** a la documentación para desarrolladores.

4

O entregar el flujo de trabajo a un agente de programación

Haz clic en **Crea con tu agente** para copiar un resumen del flujo de trabajo abierto y luego pégalo en tu agente de programación.

Comfy API empaqueta los nodos personalizados, los modelos y las dependencias de Python del flujo de trabajo en una compilación reproducible y luego la ejecuta como un endpoint con escalado automático. Consulta [Comfy API](https://docs.comfy.org/es/development/serverless/quickstart) para conocer el flujo de compilación e implementación.

### 

​

Crea con tu agente

**Crea con tu agente** es la alternativa a compilar a mano. Copia un resumen en texto plano y no ejecuta ningún comando. ComfyUI también descarga el JSON del flujo de trabajo para que tu agente tenga el archivo desde el que compilar. En la aplicación Desktop no descarga un archivo aparte: el resumen apunta a la instantánea más reciente del directorio `.launcher/snapshots` de la instalación de Desktop, e importar esa instantánea envía su JSON al compilador de la misma manera. El resumen indica las clases de nodo, los paquetes de nodos y los modelos del flujo de trabajo, y dirige a tu agente a la receta actual `comfy skills show comfy-build`, que se encarga de los comandos de comfy-cli, las versiones fijadas, el corte de la versión y cómo leer un fallo. Tu agente te confirma antes de subir el flujo de trabajo y de nuevo antes del primer corte. Luego corrige una causa por corte, te indica la causa, la edición exacta y qué compilación es antes de cada nuevo corte, y se detiene después de tres cortes. Una versión no es una implementación, así que el resumen se detiene en una versión verde y la implementación sigue siendo una decisión aparte.

## 

​

Siguiente paso: ejecutar flujos de trabajo contra el despliegue

Una vez que un despliegue está activo, consulta [Ejecutar flujos de trabajo](https://docs.comfy.org/es/development/run-workflows/overview) para llamarlo desde tu aplicación. Los [SDK de Comfy](https://docs.comfy.org/es/development/api-development/sdks) funcionan con todos los objetivos de despliegue; las instancias autoalojadas además necesitan el [API Proxy](https://docs.comfy.org/es/development/comfyui-server/api-proxy) para servir la API v2 de Comfy.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/deploy/overview.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/deploy/overview)

[Ejemplos](https://docs.comfy.org/es/development/examples)[Inicio rápido](https://docs.comfy.org/es/development/serverless/quickstart)
