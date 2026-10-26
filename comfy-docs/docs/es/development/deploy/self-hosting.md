---
url: https://docs.comfy.org/es/development/deploy/self-hosting/
title: Opciones de autoalojamiento - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:27.851883+00:00
---

# Opciones de autoalojamiento - ComfyUI

> Source: https://docs.comfy.org/es/development/deploy/self-hosting/

## En esta página

Volver arriba

  * Tu propio hardware
  * Proveedores de GPU en la nube
  * Imágenes Docker de la comunidad
  * Siguiente paso: ejecutar flujos de trabajo contra él



Opciones de autoalojamiento

# Opciones de autoalojamiento

Copiar páginaCopiar página

Ejecuta tu propio despliegue de ComfyUI: hardware propio, GPU en la nube como Runpod o Vast.ai, o Imágenes Docker de la comunidad

Copiar páginaCopiar página

Autoalojar significa ejecutar ComfyUI por tu cuenta y llamarlo como una API. Tú administras el hardware, los modelos y los Nodos personalizados, y a cambio obtienes control total: cualquier GPU, cualquier modelo, cualquier Paquete de Nodos, y tus datos nunca salen de tu infraestructura. ComfyUI se ejecuta como servidor HTTP de forma predeterminada, así que cualquier instalación funcional ya es un endpoint de API. Las opciones siguientes solo difieren en dónde vive esa instalación.

## 

​

Tu propio hardware

El despliegue más sencillo es la máquina que tienes enfrente. Instala ComfyUI y servirá `http://127.0.0.1:8188` de inmediato:

  * [Instalación manual](https://docs.comfy.org/es/installation/manual_install) para Linux, macOS y Windows, y la opción estándar para servidores
  * [Comfy Desktop](https://docs.comfy.org/es/installation/desktop/overview) o la [compilación portátil para Windows](https://docs.comfy.org/es/installation/comfyui_portable_windows) para desarrollo local

Para ejecutarlo sin navegador o escuchar en una dirección distinta de la predeterminada, consulta los [flags de inicio del servidor](https://docs.comfy.org/es/development/comfyui-server/startup-flags). Por ejemplo:
    
    
    python main.py --listen 0.0.0.0 --port 8188
    

El servidor de ComfyUI no tiene autenticación de forma predeterminada. Solo enlaza a una dirección que no sea loopback en una red de confianza, o coloca un proxy inverso con autenticación frente a él.

## 

​

Proveedores de GPU en la nube

Si no tienes una GPU propia, puedes alquilar una y ejecutar ComfyUI en ella. Entre los proveedores que suele usar la comunidad están:

  * **[Runpod](https://www.runpod.io)** : pods de GPU con Plantillas de ComfyUI de la comunidad que vienen preconfiguradas.
  * **[Vast.ai](https://vast.ai)** : un mercado de GPU; aquí también hay Plantillas de ComfyUI de la comunidad.

En estos proveedores normalmente empiezas desde una Plantilla o Imagen de la comunidad y luego agregas tus Modelos y Nodos personalizados. El resultado es un ComfyUI autoalojado normal, con una URL pública o un túnel SSH delante.

Estas Plantillas las mantiene la comunidad; no las publica ni les da soporte el Equipo de ComfyUI. Revisa qué instala una Plantilla antes de poner credenciales o modelos privados en ella.

Si quieres una Versión administrada de este flujo de trabajo, sigue el [Inicio rápido de Comfy API](https://docs.comfy.org/es/development/serverless/quickstart) para crearlo y desplegarlo en la Developer Platform.

## 

​

Imágenes Docker de la comunidad

**Docker:** ComfyUI no proporciona una imagen oficial de Docker. Si quieres ejecutar ComfyUI en un contenedor, puedes usar las imágenes mantenidas por la comunidad en [Docker Hub](https://hub.docker.com/search?q=comfyui). Estas imágenes **no están mantenidas oficialmente por Comfy-Org** y no cuentan con el soporte del equipo de ComfyUI. Úsalas bajo tu propio riesgo.

Un ComfyUI en contenedor se comporta como cualquier otra instalación autoalojada: expón el puerto del servidor y llámalo como de costumbre.

## 

​

Siguiente paso: ejecutar flujos de trabajo contra él

Puedes llamar a un despliegue autoalojado de dos maneras:

## Comfy SDKs + API Proxy

Usa los SDK oficiales contra tu instancia. El API Proxy, un pequeño servicio que se ejecuta junto a ComfyUI, sirve Comfy API v2.

## ComfyUI Server API

Llama directamente a la API REST y WebSocket, sin ningún servicio adicional. Toda la superficie local disponible, pero sin garantía de compatibilidad entre versiones.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/deploy/self-hosting.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/deploy/self-hosting)

[Uso y límites](https://docs.comfy.org/es/development/deploy/cloud-usage)[Descripción general del servidor](https://docs.comfy.org/es/development/comfyui-server/comms_overview)
