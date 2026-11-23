---
url: https://docs.comfy.org/es/development/comfy-router/models/kelly/kelly-seedance-2-0-fast/code/
title: Usa Kelly Seedance 2.0 Fast con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-23T19:03:21.380548+00:00
---

# Usa Kelly Seedance 2.0 Fast con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/kelly/kelly-seedance-2-0-fast/code/

## En esta página

Volver arriba

  * Configuración de la solicitud
  * Esquema
    * Entrada
    * Salida
  * Antes de lanzar



Kelly

# Usa Kelly Seedance 2.0 Fast con Comfy Router

Copiar páginaCopiar página

Llama a kelly/kelly-seedance-2.0-fast con Comfy Router: endpoint, forma de la solicitud y respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de API para `kelly/kelly-seedance-2.0-fast`, que Comfy Router sirve desde Kelly. **Entrada:** Texto, Imagen, Video, Audio · **Salida:** Video + Audio

## Configuración de la solicitud

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Para Python, ejecuta `pip install comfy-sdk`. Para TypeScript, ejecuta `npm install @comfyorg/sdk`. cURL usa HTTP sin procesar. **ID del modelo:** `kelly/kelly-seedance-2.0-fast` **Endpoint:** `POST https://api.comfy.org/v2/models/kelly/kelly-seedance-2.0-fast`

Router no ha publicado un esquema de entrada autorado para este modelo, así que no hay un ejemplo de solicitud del cual generar un fragmento. Router reenvía el cuerpo a Kelly sin cambios: constrúyelo a partir de la documentación de API de Kelly y envíalo con la [guía de inicio rápido de Router](https://docs.comfy.org/es/development/comfy-router/quickstart).

## Esquema

### Entrada

Router aún no ha publicado un esquema de entrada autorado para este modelo: `GET /v2/models/kelly/kelly-seedance-2.0-fast/openapi.json` devuelve un objeto abierto con `x-comfy-input-schema-authored: false`. Router reenvía el cuerpo a Kelly sin cambios, por lo que la documentación de API de Kelly es la autoridad para los campos de la solicitud y Router no realiza validación de entrada específica del modelo. La validación del proveedor sigue aplicando.

### Salida

_Este esquema no declara propiedades con nombre._

## Antes de lanzar

Los SDK crean una `Idempotency-Key` y la reutilizan para los reintentos automáticos. Para los reintentos manuales, reutiliza la clave original. Router puede mantener la conexión abierta hasta 10 minutos. Cuando una solicitud falla, Router envía un encabezado de respuesta `X-Comfy-Error-Type` que explica el motivo. Un `422` significa que Router rechazó la entrada antes de llamar al proveedor, y un `413` significa que el cuerpo de la solicitud era más grande de lo que Router acepta. Descarga los recursos generados de inmediato, porque [las URL de resultados pueden caducar](https://docs.comfy.org/es/development/comfy-router/reference#recursos-del-resultado). Cualquier límite de tamaño mencionado en la descripción de un campo más arriba es el límite propio del proveedor para ese campo, citado de la especificación del proveedor. Router aplica un tope aparte al cuerpo completo de la solicitud, con el que cuentan los medios codificados en base64: consulta [tamaño del cuerpo de la solicitud](https://docs.comfy.org/es/development/comfy-router/limitations#los-cuerpos-de-las-solicitudes-tienen-un-l%C3%ADmite). Esta página documenta un modelo socio al que se llama a través de Comfy Router. El mismo paquete `comfy-sdk` / `@comfyorg/sdk` también incluye un segundo cliente, para ejecutar todo un gráfico de flujo de trabajo de ComfyUI en Comfy Cloud: `Comfy(api_key=...)` / `new Comfy({ apiKey })`, con `client.workflows`, `client.assets` y `client.jobs`. Consulta [SDK de Comfy](https://docs.comfy.org/es/development/api-development/sdks).

## Encabezados

Autenticación, idempotencia, IDs de solicitud, agrupaciones de errores, ritmo de reintentos y límites de gasto.

## Uso de la API de Router

Descubrimiento de modelos, errores de validación, reintentos y facturación.

## Limitaciones

Lo que Router no hace hoy y qué usar en su lugar.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/kelly/kelly-seedance-2-0-fast/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/kelly/kelly-seedance-2-0-fast/code)

[Kelly Kling 4.0](https://docs.comfy.org/es/development/comfy-router/models/kelly/kelly-kling-4-0/code)[Kelly Seedance 2.0](https://docs.comfy.org/es/development/comfy-router/models/kelly/kelly-seedance-2-0/code)
