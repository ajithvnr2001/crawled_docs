---
url: https://docs.comfy.org/es/development/comfy-router/models/elevenlabs/eleven-sfx-v2/code/
title: Usa Eleven Sfx V2 con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:02.443477+00:00
---

# Usa Eleven Sfx V2 con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/elevenlabs/eleven-sfx-v2/code/

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



Elevenlabs

# Usa Eleven Sfx V2 con Comfy Router

Copiar páginaCopiar página

Llama a elevenlabs/eleven_sfx_v2 con Comfy Router: endpoint, forma de la solicitud y la respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de API para `elevenlabs/eleven_sfx_v2`, servida por Comfy Router desde Elevenlabs. **Entrada:** Texto · **Salida:** Audio

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada por HTTP directo. **ID del modelo:** `elevenlabs/eleven_sfx_v2` **Endpoint:** `POST https://api.comfy.org/v2/models/elevenlabs/eleven_sfx_v2`

  * Esperar el resultado

  * Encolar y recoger más tarde




Python

TypeScript

cURL
    
    
    from comfy_sdk import Comfy
    
    # Lee COMFY_API_KEY del entorno.
    # El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    with Comfy() as client:
        result = client.models.run(
            "elevenlabs/eleven_sfx_v2",
            {
                "duration_seconds": 5,
                "text": "A distant rumble of thunder rolling across a valley.",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    const { data } = await comfy.models.run("elevenlabs/eleven_sfx_v2", {
      duration_seconds: 5,
      text: "A distant rumble of thunder rolling across a valley.",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/elevenlabs/eleven_sfx_v2 \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"duration_seconds\": 5, \"text\": \"A distant rumble of thunder rolling across a valley.\"}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/elevenlabs/eleven_sfx_v2/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recoge cuando está listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) explica el estado, la cancelación y la recogida.

Python

TypeScript

cURL
    
    
    import asyncio
    from comfy_sdk import AsyncComfy
    
    # Lee COMFY_API_KEY del entorno.
    # Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza para los reintentos automáticos.
    async def main():
        async with AsyncComfy() as client:
            handle = await client.models.submit(
                "elevenlabs/eleven_sfx_v2",
                {
                    "duration_seconds": 5,
                    "text": "A distant rumble of thunder rolling across a valley.",
                },
            )
            print("request_id:", handle.request_id)  # junto con el ID del modelo, es todo lo que necesita otro proceso
    
            # Sondea hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
            async for update in handle.iter_events():
                print(update.status, update.queue_position)
    
            # La carga propia del proveedor, el mismo valor que devuelve models.run().
            # Una solicitud que falló o se canceló lanza aquí el error tipado de Router.
            result = await handle.get()
    
        print(result)
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza para los reintentos automáticos.
    const handle = await comfy.models.submit("elevenlabs/eleven_sfx_v2", {
      duration_seconds: 5,
      text: "A distant rumble of thunder rolling across a valley.",
    });
    console.log("requestId:", handle.requestId); // junto con el ID del modelo, es todo lo que necesita otro proceso
    
    // Sondea hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud que falló o se canceló se rechaza aquí.
    const result = await handle.get();
    
    console.log(result.data);
    
    
    
    # 1. Envía. Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/elevenlabs/eleven_sfx_v2/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"duration_seconds\": 5, \"text\": \"A distant rumble of thunder rolling across a valley.\"}"
    
    # 2. Sondea hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/elevenlabs/eleven_sfx_v2/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge. 200 con la salida nativa del modelo, 202 con el cuerpo de estado mientras aún se ejecuta.
    curl https://api.comfy.org/v2/models/elevenlabs/eleven_sfx_v2/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Esquema

### 

​

Entrada

​

duration_seconds

number

requerido

La duración del sonido que se generará, en segundos. Debe ser como mínimo 0.5 y como máximo 30. REQUERIDO en esta ruta: a diferencia de la API de ElevenLabs upstream, que adivina una duración óptima cuando el campo es null, esta ruta rechaza con 400 “Duration is required” cualquier solicitud que lo omita. El campo sigue siendo anulable solo para que un null explícito sea un documento bien formado; aun así se rechaza. Este valor es la cantidad sobre la que se mide la solicitud.Rango: `0.5` a `30`Formato: `double`

​

loop

boolean

predeterminado:"false"

Indica si se debe crear un efecto de sonido que se repita en bucle de forma fluida. ElevenLabs documenta esto como disponible únicamente para el modelo ‘eleven_text_to_sound_v2’, que es el modelo al que esta ruta reenvía ‘eleven_sfx_v2’ (consulta model_id), así que aplica aquí.

​

model_id

string

El ID del modelo que se usará para la generación de sonido. Esta ruta admite ‘eleven_sfx_v2’ y nada más; cualquier otro valor se rechaza con 400 antes de que la solicitud llegue a ElevenLabs. ‘eleven_sfx_v2’ es el id de Comfy para el modelo que ElevenLabs llama ‘eleven_text_to_sound_v2’; el proxy reescribe el cuerpo reenviado a esa denominación del proveedor, que el enum propio de ElevenLabs exige (rechaza ‘eleven_sfx_v2’ con 422), de modo que quien llama nunca envía el id del proveedor. NO está en la lista `required` de este esquema porque Comfy Router lo rellena desde el segmento de ruta `{model}` de /v2/models/elevenlabs/{model}, así que quien llama a través de Router lo omite.

​

prompt_influence

number

Una mayor influencia del prompt hace que tu generación siga el prompt más de cerca y que las generaciones sean menos variables. Debe ser un valor entre 0 y 1. El valor predeterminado es 0.3.Rango: `0` a `1`Formato: `double`

​

text

string

requerido

El texto que se convertirá en un efecto de sonido.

Generado a partir del esquema que Router sirve en `GET /v2/models/elevenlabs/eleven_sfx_v2/openapi.json`, el mismo documento con el que valida una llamada antes de que la solicitud llegue al proveedor.

### 

​

Salida

​

*/*

string (binary)

Bytes de audio sin procesar. El Content-Type y la codificación siguen el output_format solicitado y se reenvían desde ElevenLabs. El ejemplo es un marcador de posición del cuerpo binario, no JSON ni base64.

## 

​

Ejemplos

### 

​

Entrada
    
    
    {
      "duration_seconds": 5,
      "text": "A distant rumble of thunder rolling across a valley."
    }
    

### 

​

Salida

Cuerpo binario: bytes sin procesar en lugar de un documento JSON, devuelto como `*/*`, por lo que no hay un ejemplo JSON que mostrar. El `Content-Type` y la codificación de la respuesta dependen de la solicitud, tal como describe el esquema de Salida anterior.

## 

​

Antes de lanzar

Los SDK crean una `Idempotency-Key` y la reutilizan para los reintentos automáticos. Para los reintentos manuales, reutiliza la clave original. Router puede mantener la conexión abierta hasta 10 minutos. Cuando una solicitud falla, Router envía un encabezado de respuesta `X-Comfy-Error-Type` que explica el motivo. Un `422` significa que Router rechazó la entrada antes de llamar al proveedor, y un `413` significa que el cuerpo de la solicitud era más grande de lo que Router acepta. Descarga los recursos generados de inmediato, porque [las URL de resultados pueden caducar](https://docs.comfy.org/es/development/comfy-router/reference#recursos-del-resultado). Cualquier límite de tamaño mencionado en la descripción de un campo más arriba es el límite propio del proveedor para ese campo, citado de la especificación del proveedor. Router aplica un tope aparte al cuerpo completo de la solicitud, con el que cuentan los medios codificados en base64: consulta [tamaño del cuerpo de la solicitud](https://docs.comfy.org/es/development/comfy-router/limitations#los-cuerpos-de-las-solicitudes-tienen-un-l%C3%ADmite). Esta página documenta un modelo socio al que se llama a través de Comfy Router. El mismo paquete `comfy-sdk` / `@comfyorg/sdk` también incluye un segundo cliente, para ejecutar todo un gráfico de flujo de trabajo de ComfyUI en Comfy Cloud: `Comfy(api_key=...)` / `new Comfy({ apiKey })`, con `client.workflows`, `client.assets` y `client.jobs`. Consulta [SDK de Comfy](https://docs.comfy.org/es/development/api-development/sdks).

## Encabezados

Autenticación, idempotencia, IDs de solicitud, agrupaciones de errores, ritmo de reintentos y límites de gasto.

## Uso de la API de Router

Descubrimiento de modelos, errores de validación, reintentos y facturación.

## Limitaciones

Lo que Router no hace hoy y qué usar en su lugar.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/elevenlabs/eleven-sfx-v2/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/elevenlabs/eleven-sfx-v2/code)

[Eleven Multilingual V2](https://docs.comfy.org/es/development/comfy-router/models/elevenlabs/eleven-multilingual-v2/code)[Eleven V3](https://docs.comfy.org/es/development/comfy-router/models/elevenlabs/eleven-v3/code)
