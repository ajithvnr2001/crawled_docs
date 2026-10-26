---
url: https://docs.comfy.org/es/development/cloud/openapi/
title: Especificaci\u00f3n OpenAPI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:52.579574+00:00
---

# Especificación OpenAPI - ComfyUI

> Source: https://docs.comfy.org/es/development/cloud/openapi/

## En esta página

Volver arriba

  * Especificación de la API de Comfy Cloud
  * Referencia interactiva de la API
  * Usar la especificación
  * Descargar
  * Autenticación
    * Obtener una clave API
    * Usar la clave API
  * URL base
  * Conexión WebSocket



v1 Cloud API (deprecated)

# Especificación OpenAPI

Copiar páginaCopiar página

Especificación OpenAPI legible por máquina para la API de Comfy Cloud

Copiar páginaCopiar página

**Obsoleto:** la API v1 de Cloud está obsoleta en favor de [Comfy API v2](https://docs.comfy.org/es/api-reference/v2/overview). Los endpoints, los formatos de solicitud y respuesta, y el comportamiento pueden modificarse sin previo aviso.

# 

​

Especificación de la API de Comfy Cloud

Esta página proporciona la especificación completa de OpenAPI 3.0 para la API de Comfy Cloud.

**Suscripción requerida:** ejecutar flujos de trabajo mediante la API requiere una suscripción activa a Comfy Cloud. Consulta los [planes de precios](https://www.comfy.org/cloud/pricing?utm_source=docs&utm_campaign=cloud-api) para obtener más detalles.

## 

​

Referencia interactiva de la API

Explora la API completa con documentación interactiva:

## Referencia de la API de Cloud

Explora los endpoints, consulta los esquemas y prueba solicitudes

## 

​

Usar la especificación

La especificación OpenAPI sirve para:

  * **Generar bibliotecas cliente** en cualquier idioma con herramientas como [OpenAPI Generator](https://openapi-generator.tech/)
  * **Importar en herramientas de API** como Postman, Insomnia o Paw
  * **Generar documentación** con herramientas como Redoc o Swagger UI
  * **Validar solicitudes** en tu aplicación



## 

​

Descargar

Puedes descargar el archivo de especificación OpenAPI sin procesar:

## openapi-cloud.yaml

Descarga la especificación OpenAPI 3.0

## 

​

Autenticación

Todas las solicitudes a la API requieren una clave API que se envía en el encabezado `X-API-Key`.

### 

​

Obtener una clave API

Consulta [Obtener una clave API](https://docs.comfy.org/es/development/api-development/getting-an-api-key) para ver instrucciones paso a paso con capturas de pantalla.

### 

​

Usar la clave API
    
    
    X-API-Key: your-api-key
    

## 

​

URL base

Entorno| URL  
---|---  
Producción| `https://cloud.comfy.org`  
  
## 

​

Conexión WebSocket

Para recibir actualizaciones en tiempo real, conéctate al endpoint de WebSocket:
    
    
    wss://cloud.comfy.org/ws?clientId={uuid}&token={api_key}
    

Consulta la [Referencia de la API de Cloud](https://docs.comfy.org/es/development/cloud/api-reference#websocket-para-el-progreso-en-tiempo-real) para conocer los tipos de mensajes y cómo manejarlos.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/cloud/openapi.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/cloud/openapi)

[Ejemplos de código](https://docs.comfy.org/es/development/cloud/api-reference)[Get information about current prompt executions](https://docs.comfy.org/es/api-reference/cloud/workflow/get-information-about-current-prompt-executions)
