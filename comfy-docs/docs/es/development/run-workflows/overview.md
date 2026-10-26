---
url: https://docs.comfy.org/es/development/run-workflows/overview/
title: Ejecutar flujos de trabajo - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:28.225301+00:00
---

# Ejecutar flujos de trabajo - ComfyUI

> Source: https://docs.comfy.org/es/development/run-workflows/overview/

## En esta página

Volver arriba

  * Empieza aquí: los SDK de Comfy
  * Qué funciona con qué
  * ¿Qué API debería usar?
  * Primeros pasos
  * Requisitos previos



Ejecutar flujos de trabajo

# Ejecutar flujos de trabajo

Copiar páginaCopiar página

Cómo ejecutar flujos de trabajo de ComfyUI en una implementación activa y qué cliente funciona con cada una

Copiar páginaCopiar página

Una vez que ComfyUI está [desplegado en algún lugar](https://docs.comfy.org/es/development/deploy/overview), tu aplicación ejecuta flujos de trabajo contra él: envía un flujo de trabajo, espera la ejecución y descarga las salidas. Esta página describe qué cliente usar para cada despliegue.

## 

​

Empieza aquí: los SDK de Comfy

Para una nueva integración, usa los **SDK de Comfy** oficiales (Python y TypeScript) y la [API de Comfy v2](https://docs.comfy.org/es/api-reference/v2/overview) a la que llaman. El mismo código funciona con cualquier objetivo de despliegue; solo cambia la URL base.

## Comfy SDKs

Instala un SDK para enviar flujos de trabajo y descargar salidas desde Python o TypeScript.

## 

​

Qué funciona con qué

Despliegue| SDK de Comfy / API v2| Notas  
---|---|---  
**Despliegue de Comfy API**|  Sí| Configura `COMFY_BASE_URL` para que apunte a `https://<deployment>.run.comfy.app` con tu clave API  
**Comfy Cloud**|  Sí| La URL base predeterminada. Requiere una clave API y una suscripción de pago  
**Autoalojado**|  Sí, mediante el [Proxy de API](https://docs.comfy.org/es/development/comfyui-server/api-proxy)| Un pequeño servicio junto a ComfyUI sirve la API v2  
  
Las instancias autoalojadas también pueden omitir el SDK por completo y usar directamente la [API del Servidor de ComfyUI](https://docs.comfy.org/es/development/comfyui-server/comms_overview) (REST + WebSocket). Expone toda la superficie local, incluidas la cola y la información del nodo, pero no ofrece garantía de compatibilidad entre versiones.

## 

​

¿Qué API debería usar?

| Comfy API v2 + SDKs| API de Cloud v1| API de servidor de ComfyUI  
---|---|---|---  
**Dónde se ejecuta**|  Despliegues de Comfy API, Comfy Cloud o autoalojado mediante el proxy de API| Solo en Comfy Cloud| Solo autoalojado  
**Compatibilidad**|  Versionada, solo cambios aditivos dentro de v2| Obsoleta, puede cambiar sin previo aviso| Sin garantías entre versiones  
**Autenticación**| `Authorization: Bearer` en Comfy Cloud y en los despliegues de Comfy API. Autoalojado: ninguna por defecto, token bearer estático opcional| Encabezado `X-API-Key` (cuenta de Comfy Cloud)| Ninguna (local) o Clave API para Nodos asociados  
**Clientes oficiales**|  SDKs de Python y TypeScript| Ninguno, llama por HTTP| Ninguno, llama por HTTP  
**Protocolo**|  REST + SSE| REST + WebSocket| REST + WebSocket  
**Alcance**|  Ejecutar un flujo de trabajo y obtener resultados| Superficie completa de Cloud, incluidos modelos y cuenta| Superficie local completa, incluidos la cola e Información del Nodo  
**Ideal para**|  Nuevas integraciones que deben seguir funcionando| Integraciones existentes y funciones de Cloud que v2 aún no cubre| Control total, herramientas personalizadas contra tu propia instancia  
  
Todas aceptan el mismo formato de flujo de trabajo ([formato API](https://docs.comfy.org/es/development/api-development/workflow-api-format)), así que puedes desarrollar y probar flujos de trabajo localmente y moverlos a otro despliegue sin cambios.

## 

​

Primeros pasos

## SDK de Comfy

Ejecuta flujos de trabajo desde Python o TypeScript, contra cualquier objetivo de despliegue.

## Proxy de API para autoalojado

Sirve la API v2 delante de tu propio ComfyUI para que los SDK puedan acceder a ella.

## Formato de API de flujo de trabajo

Exporta flujos de trabajo en el formato JSON que aceptan las API.

## API del servidor de ComfyUI

La API REST y WebSocket sin procesar de una instancia autoalojada.

## 

​

Requisitos previos

  * Una [clave API](https://docs.comfy.org/es/development/api-development/getting-an-api-key) para cualquier cosa que se conecte con Comfy Cloud, un despliegue de Comfy API o los Nodos asociados. Un ComfyUI que sea puramente local no la necesita.
  * Un flujo de trabajo exportado en [formato API](https://docs.comfy.org/es/development/api-development/workflow-api-format).



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/run-workflows/overview.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/run-workflows/overview)

[Autenticación de Nodos asociados](https://docs.comfy.org/es/development/comfyui-server/api-key-integration)[Primer flujo de trabajo](https://docs.comfy.org/es/development/api-development/quickstart)
