---
url: https://docs.comfy.org/es/development/comfy-router/models/typesafe/jev-1-14-0/code/
title: Usa Jev 1.14.0 con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-23T19:03:23.210825+00:00
---

# Usa Jev 1.14.0 con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/typesafe/jev-1-14-0/code/

## En esta página

Volver arriba

  * Inicio rápido
  * Esquema
    * Entrada
    * Salida
  * Ejemplos
    * Entrada
    * Salida
  * Antes de lanzar



Typesafe

# Usa Jev 1.14.0 con Comfy Router

Copiar páginaCopiar página

Llama a typesafe/jev-1.14.0 desde Comfy Router: endpoint, forma de la solicitud y respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de API para `typesafe/jev-1.14.0`, servida por Comfy Router desde Typesafe. **Entrada:** Texto, Imagen · **Salida:** Texto

## Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada por HTTP directo. **ID del modelo:** `typesafe/jev-1.14.0` **Endpoint:** `POST https://api.comfy.org/v2/models/typesafe/jev-1.14.0`

  * Espera el resultado

  * Enviar a la cola y recoger más tarde




Python

TypeScript

cURL
    
    
    from comfy_sdk import Comfy
    
    # Lee COMFY_API_KEY del entorno.
    # El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    with Comfy() as client:
        result = client.models.run(
            "typesafe/jev-1.14.0",
            {
                "questions": {
                    "department": {
                        "criteria": {
                            "billing": "Payments, invoicing, refunds",
                            "technical": "Bugs, outages, integrations",
                        },
                        "instructions": "Which team should handle this?",
                        "type": "choice",
                    },
                    "is_urgent": {
                        "instructions": "Does this convey urgency?",
                        "type": "noul",
                    },
                },
                "state": "Help! My payouts have been failing for 3 days.",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    const { data } = await comfy.models.run("typesafe/jev-1.14.0", {
      questions: {
        department: {
          criteria: {
            billing: "Payments, invoicing, refunds",
            technical: "Bugs, outages, integrations",
          },
          instructions: "Which team should handle this?",
          type: "choice",
        },
        is_urgent: {
          instructions: "Does this convey urgency?",
          type: "noul",
        },
      },
      state: "Help! My payouts have been failing for 3 days.",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/typesafe/jev-1.14.0 \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"questions\": {\"department\":{\"criteria\":{\"billing\":\"Payments, invoicing, refunds\",\"technical\":\"Bugs, outages, integrations\"},\"instructions\":\"Which team should handle this?\",\"type\":\"choice\"},\"is_urgent\":{\"instructions\":\"Does this convey urgency?\",\"type\":\"noul\"}}, \"state\": \"Help! My payouts have been failing for 3 days.\"}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/typesafe/jev-1.14.0/requests`. Router responde `201` con un `request_id` en cuanto la ejecución es admitida, y el resultado se recoge cuando está listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) recorre el estado, la cancelación y la recogida.

Python

TypeScript

cURL
    
    
    import asyncio
    from comfy_sdk import AsyncComfy
    
    # Lee COMFY_API_KEY del entorno.
    # Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza en los reintentos automáticos.
    async def main():
        async with AsyncComfy() as client:
            handle = await client.models.submit(
                "typesafe/jev-1.14.0",
                {
                    "questions": {
                        "department": {
                            "criteria": {
                                "billing": "Payments, invoicing, refunds",
                                "technical": "Bugs, outages, integrations",
                            },
                            "instructions": "Which team should handle this?",
                            "type": "choice",
                        },
                        "is_urgent": {
                            "instructions": "Does this convey urgency?",
                            "type": "noul",
                        },
                    },
                    "state": "Help! My payouts have been failing for 3 days.",
                },
            )
            print("request_id:", handle.request_id)  # junto con el ID del modelo, es todo lo que necesita otro proceso
    
            # Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
            async for update in handle.iter_events():
                print(update.status, update.queue_position)
    
            # El payload propio del proveedor, el mismo valor que devuelve models.run().
            # Una solicitud que falló o se canceló lanza aquí el error tipado de Router.
            result = await handle.get()
    
        print(result)
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza en los reintentos automáticos.
    const handle = await comfy.models.submit("typesafe/jev-1.14.0", {
      questions: {
        department: {
          criteria: {
            billing: "Payments, invoicing, refunds",
            technical: "Bugs, outages, integrations",
          },
          instructions: "Which team should handle this?",
          type: "choice",
        },
        is_urgent: {
          instructions: "Does this convey urgency?",
          type: "noul",
        },
      },
      state: "Help! My payouts have been failing for 3 days.",
    });
    console.log("requestId:", handle.requestId); // junto con el ID del modelo, es todo lo que necesita otro proceso
    
    // Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud que falló o se canceló se rechaza aquí.
    const result = await handle.get();
    
    console.log(result.data);
    
    
    
    # 1. Envía. Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/typesafe/jev-1.14.0/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"questions\": {\"department\":{\"criteria\":{\"billing\":\"Payments, invoicing, refunds\",\"technical\":\"Bugs, outages, integrations\"},\"instructions\":\"Which team should handle this?\",\"type\":\"choice\"},\"is_urgent\":{\"instructions\":\"Does this convey urgency?\",\"type\":\"noul\"}}, \"state\": \"Help! My payouts have been failing for 3 days.\"}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/typesafe/jev-1.14.0/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge. 200 con la salida nativa del modelo, 202 con el cuerpo de estado mientras sigue en ejecución.
    curl https://api.comfy.org/v2/models/typesafe/jev-1.14.0/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## Esquema

### Entrada

assets

object

Las imágenes de la solicitud, con una cadena de referencia como clave. Cada referencia debe aparecer en algún lugar de `state`, `instructions` o `criteria`. Cada imagen es un PNG o JPEG estático de 280 a 1568 píxeles por lado y como máximo 16 MiB después de la decodificación; TypeSafe rechaza una llamada que supere los 32 MiB en total.

model

string

La versión fijada de Jev. Es opcional: Router la completa a partir del id del modelo en la ruta. No se aceptan los alias `jev-latest` y `jev-preview`.

questions

object

requerido

Las preguntas que se deben responder, con un id que elijas como clave. La respuesta a cada una se devuelve con el mismo id.

state

object

requerido

El contenido que se va a evaluar: una cadena o datos estructurados (un objeto o un arreglo) de hasta 64 niveles de profundidad. Cualquier referencia a un recurso que aparezca en él se reemplaza por esa imagen.

Generado a partir del esquema que Router sirve en `GET /v2/models/typesafe/jev-1.14.0/openapi.json`, el mismo documento con el que valida una llamada antes de que la solicitud llegue al proveedor.

### Salida

answers

object

requerido

Una respuesta por pregunta, identificadas por los ids de pregunta que enviaste.

model

string

requerido

La versión de Jev que respondió, por ejemplo `jev-1.14.0`.

usage

object

Uso de tokens de la solicitud.

usage.input_tokens

integer

Tokens de entrada, incluida cada imagen de la solicitud.

usage.output_tokens

integer

Tokens de salida.

## Ejemplos

### Entrada
    
    
    {
      "questions": {
        "department": {
          "criteria": {
            "billing": "Payments, invoicing, refunds",
            "technical": "Bugs, outages, integrations"
          },
          "instructions": "Which team should handle this?",
          "type": "choice"
        },
        "is_urgent": {
          "instructions": "Does this convey urgency?",
          "type": "noul"
        }
      },
      "state": "Help! My payouts have been failing for 3 days."
    }
    

### Salida
    
    
    {
      "answers": {
        "is_urgent": {
          "noul": 0.95,
          "type": "noul"
        },
        "mug": {
          "box": {
            "bottom": 0.82,
            "left": 0.44,
            "right": 0.84,
            "top": 0.25
          },
          "confidence": 0.92,
          "type": "box"
        }
      },
      "model": "jev-1.14.0",
      "usage": {
        "input_tokens": 290,
        "output_tokens": 21
      }
    }
    

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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/typesafe/jev-1-14-0/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/typesafe/jev-1-14-0/code)

[Jev 1.13.0](https://docs.comfy.org/es/development/comfy-router/models/typesafe/jev-1-13-0/code)[Clean Audio Video](https://docs.comfy.org/es/development/comfy-router/models/veed/clean-audio-video/code)
