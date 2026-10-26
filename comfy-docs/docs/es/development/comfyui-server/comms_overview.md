---
url: https://docs.comfy.org/es/development/comfyui-server/comms_overview/
title: Descripci\u00f3n general del servidor - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:27.442771+00:00
---

# Descripción general del servidor - ComfyUI

> Source: https://docs.comfy.org/es/development/comfyui-server/comms_overview/

## En esta página

Volver arriba

  * Iniciar el servidor
  * Páginas clave en esta sección
  * Usar nodos asociados
  * Cómo funciona el servidor



Self-Hosted Server API

# Descripción general del servidor

Copiar páginaCopiar página

Ejecuta ComfyUI como servidor e interactúa con él mediante las APIs REST y WebSocket

Copiar páginaCopiar página

ComfyUI se ejecuta de forma predeterminada como un servidor HTTP en tu máquina. Puedes llamarlo de forma programática para enviar flujos de trabajo, subir archivos, descargar salidas y monitorear el progreso, todo sin abrir el navegador.

## 

​

Iniciar el servidor

Cuando inicias ComfyUI, se inicia automáticamente un servidor HTTP en `http://127.0.0.1:8188`. Para ejecutar ComfyUI como servidor sin interfaz gráfica (sin navegador):
    
    
    # Ejecutar sin abrir el navegador
    python main.py --disable-auto-launch
    
    
    
    # Especificar un puerto personalizado
    python main.py --port 8288
    
    
    
    # Escuchar en todas las interfaces de red (para acceso remoto)
    python main.py --listen 0.0.0.0
    

Para ver una lista completa de las opciones de inicio, ejecuta `python main.py --help` o consulta la [Referencia de flags de inicio](https://docs.comfy.org/es/development/comfyui-server/startup-flags).

## 

​

Páginas clave en esta sección

## Argumentos de inicio

Referencia completa de todos los argumentos de línea de comandos de main.py.

## Rutas de la API

Endpoints HTTP disponibles para enviar flujos de trabajo, subir archivos y consultar el estado.

## Ejemplos de API

Ejemplos de código para llamar a la API: solo HTTP, WebSocket + History y SaveImageWebsocket.

## Mensajes del servidor

Tipos de mensajes WebSocket que el servidor envía al cliente durante la ejecución.

## Inversión del modelo de ejecución

Avanzado: invierte la ejecución para flujos de control personalizados.

## 

​

Usar nodos asociados

Si tu flujo de trabajo contiene nodos asociados de pago, puedes incluir tu clave API en el payload. Consulta la guía [Integración de la API de nodos asociados](https://docs.comfy.org/es/development/comfyui-server/api-key-integration) para obtener más detalles.

* * *

## 

​

Cómo funciona el servidor

El servidor de Comfy se ejecuta sobre el [framework aiohttp](https://docs.aiohttp.org/), que a su vez utiliza [asyncio](https://pypi.org/project/asyncio/). Los mensajes del servidor al cliente se envían mediante mensajes de socket a través del método `send_sync` del servidor, que es una instancia de `PromptServer` (definida en `server.py`). Un escucha de eventos de socket registrado en `api.js` los procesa. Consulta [mensajes](https://docs.comfy.org/es/development/comfyui-server/comms_messages). Los mensajes del cliente al servidor se envían mediante el método `api.fetchApi()` definido en `api.js`, y los manejan las rutas HTTP definidas por el servidor. Consulta [rutas](https://docs.comfy.org/es/development/comfyui-server/comms_routes).

El cliente envía todo el flujo de trabajo (los valores de los widgets y todo lo demás) cuando pones una solicitud en cola. El servidor no recibe ningún cambio que hagas después de enviar una solicitud a la cola. Si quieres modificar el comportamiento del servidor durante la ejecución, necesitarás rutas.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfyui-server/comms_overview.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfyui-server/comms_overview)

[Opciones de alojamiento](https://docs.comfy.org/es/development/deploy/self-hosting)[Ejemplos de API](https://docs.comfy.org/es/development/comfyui-server/api-examples)
