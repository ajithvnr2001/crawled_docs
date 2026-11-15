---
url: https://docs.comfy.org/es/development/deploy/overview/
title: Implementar ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-15T14:36:25.461039+00:00
---

# Implementar ComfyUI - ComfyUI

> Source: https://docs.comfy.org/es/development/deploy/overview/

## En esta página

Volver arriba

  * Implementar desde la aplicación ComfyUI
  * Ejecutar una implementación desde el editor de Cloud
  * Ejecutar flujos de trabajo desde tu aplicación



Desplegar ComfyUI

# Implementar ComfyUI

Copiar páginaCopiar página

Compara Comfy Cloud, las implementaciones gestionadas de la API de Comfy y el autoalojamiento para elegir cómo ejecutar ComfyUI.

Copiar páginaCopiar página

Puedes ejecutar tus flujos de trabajo de ComfyUI en Comfy Cloud, en tu propia implementación de Comfy API o en un servidor que administres. Comfy Cloud y Comfy API se ejecutan en GPU de Comfy, así que no necesitas una GPU en tu equipo. Elige la opción que encaje con tu flujo de trabajo y empieza desde su tarjeta.

## Comfy Cloud

Ejecuta flujos de trabajo cuyos nodos personalizados y modelos ya están en Comfy Cloud, sin crear un build ni un despliegue.

## Builds personalizados en Comfy Cloud

Ejecuta flujos de trabajo que necesitan tus propios nodos personalizados y modelos dentro del editor de Comfy Cloud, con un build que creas en tu navegador.

## Comfy API

Empaqueta nodos personalizados, modelos y dependencias de Python en un build y ejecútalo como un endpoint con escalado automático.

## Autoalojamiento

Ejecuta ComfyUI en una máquina que administres y sírvelo en tu red con `--listen`.

Para llamar a cualquiera de estas opciones desde tu propio código, envía el flujo de trabajo en [formato API](https://docs.comfy.org/es/development/api-development/workflow-api-format).

## Implementar desde la aplicación ComfyUI

En ComfyUI en tu equipo o en Comfy Desktop, la tarjeta **Deploy to Comfy API** inicia un build de Comfy API a partir del flujo de trabajo abierto.

Publicar una versión es gratis. Cuando termina su build, la fila **Serverless build** muestra un botón **Deploy**. Al implementar se cobra almacenamiento desde el momento del despliegue, más el tiempo de GPU mientras un worker está activo. El diálogo de despliegue muestra el coste estimado antes de confirmar.

1

Abrir el menú Workflow actions

En la **Top bar** , haz clic derecho en la pestaña del flujo de trabajo. También puedes hacer clic en el botón **Workflow actions** de la esquina superior izquierda del **Canvas**.![Menú Workflow actions abierto desde una pestaña de flujo de trabajo, con Deploy to Comfy API y su insignia NEW debajo de Export \(API\)](https://mintcdn.com/dripart/oPsov_e3HUhk_xUX/images/development/deploy/deploy-to-comfy-api.png?fit=max&auto=format&n=oPsov_e3HUhk_xUX&q=85&s=8ad6bb82f3d9d29016e1cb51addbfdf3)

2

Seleccionar Deploy to Comfy API

Selecciona **Deploy to Comfy API**. La entrada está marcada como **NEW**. Se abre la tarjeta **Deploy to Comfy API** y cuenta los paquetes de nodos, los modelos y las clases de nodo que usa el flujo de trabajo.![Tarjeta Deploy to Comfy API con un vídeo del producto, los recuentos de paquetes de nodos, modelos y clases de nodo, y el botón Deploy on Platform](https://mintcdn.com/dripart/oPsov_e3HUhk_xUX/images/development/deploy/deploy-api-ui.png?fit=max&auto=format&n=oPsov_e3HUhk_xUX&q=85&s=ec4345b0864c7777b8b8c11afb17ae75)

3

Continuar en Developer Platform

Haz clic en **Deploy on Platform**. Developer Platform en [platform.comfy.org](https://platform.comfy.org) se abre en una pestaña nueva.

En Developer Platform, creas un build a partir del flujo de trabajo, publicas una versión y la implementas. [Orígenes de compilación](https://docs.comfy.org/es/development/serverless/build-sources) cubre cómo iniciar un build desde un archivo de flujo de trabajo, y la [guía rápida de Comfy API](https://docs.comfy.org/es/development/serverless/quickstart) cubre el mismo flujo con comfy-cli.

## Ejecutar una implementación desde el editor de Cloud

Para crear una implementación desde el editor de Comfy Cloud, ejecutar tus flujos de trabajo en ella y detenerla o eliminarla, consulta [Agregar builds personalizados a Comfy Cloud](https://docs.comfy.org/es/development/deploy/cloud-custom-builds).

## Ejecutar flujos de trabajo desde tu aplicación

Cuando una implementación está **Ready** , consulta [Ejecutar flujos de trabajo](https://docs.comfy.org/es/development/run-workflows/overview) para llamarla desde tu aplicación. Los [SDK de Comfy](https://docs.comfy.org/es/development/api-development/sdks) funcionan con Comfy Cloud y con tus implementaciones. Un ComfyUI autoalojado necesita el [API Proxy](https://docs.comfy.org/es/development/comfyui-server/api-proxy) para servir Comfy API v2.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/deploy/overview.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/deploy/overview)

[Ejemplos](https://docs.comfy.org/es/development/examples)[Inicio rápido](https://docs.comfy.org/es/development/serverless/quickstart)
