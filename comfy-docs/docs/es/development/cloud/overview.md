---
url: https://docs.comfy.org/es/development/cloud/overview/
title: Descripci\u00f3n general de la API de Cloud v1 - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:53.507868+00:00
---

# Descripción general de la API de Cloud v1 - ComfyUI

> Source: https://docs.comfy.org/es/development/cloud/overview/

## En esta página

Volver arriba

  * URL base
  * Autenticación
  * Lo que los SDK aún no cubren
  * Endpoints disponibles
  * Manejo de errores
  * Próximos pasos



v1 Cloud API (deprecated)

# Descripción general de la API de Cloud v1

Copiar páginaCopiar página

La superficie obsoleta de la API de Cloud v1: autenticación y los endpoints propios de Cloud que Comfy API v2 no expone

Copiar páginaCopiar página

**Obsoleto:** La API de Cloud v1 está obsoleta en favor de [Comfy API v2](https://docs.comfy.org/es/api-reference/v2/overview). Sigue disponible para las integraciones existentes y para las capacidades de Cloud que v2 aún no expone, pero los endpoints y el comportamiento pueden cambiar sin previo aviso.

La API de Cloud v1 proporciona acceso programático a [Comfy Cloud](https://docs.comfy.org/es/development/deploy/cloud), el servicio administrado de Comfy para ejecutar flujos de trabajo en infraestructura en la nube. Comfy Cloud es una aplicación con estado. Tu cuenta mantiene un estado que persiste entre tareas: créditos y nivel de suscripción, recursos subidos y salidas generadas, la cola de trabajos y el conjunto de modelos y nodos instalados. La API v1 abarca toda esa aplicación, así que incluye funcionalidad que la portable [Comfy API v2](https://docs.comfy.org/es/api-reference/v2/overview) no admite, como la gestión de la cola, la exploración de modelos, las definiciones de nodos y los endpoints de cuenta. Usa v2 (o los SDK que la envuelven) para enviar flujos de trabajo y obtener resultados de una forma que también funcione con despliegues de Comfy API y con ComfyUI autoalojado. Usa v1 para las capacidades específicas de Cloud a su alrededor. Para ejecutar flujos de trabajo, empieza con la [Guía de inicio rápido de Comfy Cloud](https://docs.comfy.org/es/development/deploy/cloud) y los [SDK de Comfy](https://docs.comfy.org/es/development/api-development/sdks). Los créditos y los límites de concurrencia se tratan en [Uso y límites](https://docs.comfy.org/es/development/deploy/cloud-usage); los ejemplos ejecutables de v1 están en la [Referencia de la API de Cloud](https://docs.comfy.org/es/development/cloud/api-reference). Esta página cubre la superficie específica de v1: la autenticación y los endpoints que v2 no expone.

**Suscripción requerida:** El acceso a la API requiere una suscripción de pago a Comfy Cloud; el nivel Gratis no lo incluye. Consulta los [planes de precios](https://www.comfy.org/cloud/pricing?utm_source=docs&utm_campaign=cloud-api).

## 

​

URL base
    
    
    https://cloud.comfy.org
    

## 

​

Autenticación

Todas las solicitudes v1 requieren una clave API enviada en el encabezado `X-API-Key`:
    
    
    curl -X GET "https://cloud.comfy.org/api/user" \
      -H "X-API-Key: $COMFY_CLOUD_API_KEY"
    

Consulta [Obtener una clave API](https://docs.comfy.org/es/development/api-development/getting-an-api-key) para ver las instrucciones sobre cómo crear y administrar claves. Una clave inválida o faltante devuelve `401`. Una clave con una suscripción inactiva devuelve `429`. La misma clave se usa para los [Nodos asociados](https://docs.comfy.org/es/tutorials/partner-nodes/overview). Por HTTP, la vuelves a pasar en `extra_data.api_key_comfy_org`; consulta [Usar Nodos asociados](https://docs.comfy.org/es/development/cloud/api-reference#usar-nodos-asociados) para ver ejemplos.

## 

​

Lo que los SDK aún no cubren

Los SDK cubren cómo ejecutar un flujo de trabajo, obtener los resultados y cancelar una tarea. El resto de la superficie de Cloud solo está disponible por HTTP, así que llama directamente a estos endpoints aunque uses un SDK para la ejecución.

Capacidad| Endpoint| Referencia  
---|---|---  
Estado de la cola, tareas en ejecución y pendientes| `GET /api/queue`| [Gestión de la cola](https://docs.comfy.org/es/development/cloud/api-reference#gesti%C3%B3n-de-la-cola)  
Interrumpir la ejecución actual| `POST /api/interrupt`| [Gestión de la cola](https://docs.comfy.org/es/development/cloud/api-reference#gesti%C3%B3n-de-la-cola)  
Definiciones de nodos y especificaciones de entradas| `GET /api/object_info`| [Información de objetos](https://docs.comfy.org/es/development/cloud/api-reference#informaci%C3%B3n-de-objetos)  
Explorar modelos disponibles| Endpoints de modelos| [Especificación OpenAPI](https://docs.comfy.org/es/development/cloud/openapi)  
Información de la cuenta y del usuario| `GET /api/user`| [Especificación OpenAPI](https://docs.comfy.org/es/development/cloud/openapi)  
Subidas de máscaras que hacen referencia a una imagen existente| `POST /api/upload/mask`| [Subir entradas](https://docs.comfy.org/es/development/cloud/api-reference#subir-entradas)  
  
Cancelar una tarea lo cubren ambos: los SDK cancelan una tarea de la que tienes un identificador, y `POST /api/queue` cancela por ID.

## 

​

Endpoints disponibles

Categoría| Descripción  
---|---  
[Flujos de trabajo](https://docs.comfy.org/es/development/cloud/api-reference#ejecutar-flujos-de-trabajo)| Envía flujos de trabajo y consulta su estado  
[Tareas](https://docs.comfy.org/es/development/cloud/api-reference#comprobar-el-estado-de-la-tarea)| Supervisa el estado y la cola de las tareas  
[Entradas](https://docs.comfy.org/es/development/cloud/api-reference#subir-entradas)| Sube imágenes, máscaras y otras entradas  
[Salidas](https://docs.comfy.org/es/development/cloud/api-reference#downloading-outputs)| Descarga el contenido generado  
[WebSocket](https://docs.comfy.org/es/development/cloud/api-reference#websocket-para-el-progreso-en-tiempo-real)| Actualizaciones de progreso en tiempo real  
[Información de objetos](https://docs.comfy.org/es/development/cloud/api-reference#informaci%C3%B3n-de-objetos)| Nodos disponibles y sus definiciones  
  
## 

​

Manejo de errores

Los endpoints REST devuelven códigos de estado HTTP estándar:

Estado| Descripción  
---|---  
`400`| Solicitud inválida (flujo de trabajo incorrecto, campos faltantes)  
`401`| No autorizado (clave API inválida o faltante)  
`402`| Créditos insuficientes  
`429`| Suscripción inactiva  
`500`| Error interno del servidor  
  
En su lugar, los SDK lanzan estas situaciones como excepciones tipadas, incluidas `Unauthorized`, `InvalidWorkflow`, `InsufficientCredits`, `QueueFull` y `JobFailed`, todas las cuales extienden `ComfyError`. Las fallas de ejecución son independientes de los errores HTTP. Consulta [Manejo de errores](https://docs.comfy.org/es/development/cloud/api-reference#manejo-de-errores) para conocer los valores de `exception_type` que se entregan durante la ejecución.

## 

​

Próximos pasos

## Comfy Cloud Quickstart

Ejecuta un flujo de trabajo desde Python o TypeScript.

## Uso y límites

Revisa los créditos de Cloud, la concurrencia y las integraciones v1 existentes.

## Referencia de la API de Cloud

Documentación completa de los endpoints con ejemplos en curl, Python y TypeScript.

## Referencia de Comfy API v2

La API HTTP versionada que sustenta ambos SDK. Úsala desde cualquier idioma.

## Especificación OpenAPI

Especificación de API legible por máquina para generar código.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/cloud/overview.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/cloud/overview)

[Request cancellation](https://docs.comfy.org/es/api-reference/v2/jobs/request-cancellation)[Ejemplos de código](https://docs.comfy.org/es/development/cloud/api-reference)
