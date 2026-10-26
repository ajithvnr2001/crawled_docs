---
url: https://docs.comfy.org/es/development/comfy-router/models/luma/photon-flash-1/code/
title: Usa Photon Flash 1 con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:10.412166+00:00
---

# Usa Photon Flash 1 con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/luma/photon-flash-1/code/

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



Luma

# Usa Photon Flash 1 con Comfy Router

Copiar páginaCopiar página

Llama a luma/photon-flash-1 desde Comfy Router: endpoint, forma de la solicitud y la respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de la API de `luma/photon-flash-1`, servida por Comfy Router desde Luma. **Entrada:** Texto · **Salida:** Imagen

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada sobre HTTP directo. **ID del modelo:** `luma/photon-flash-1` **Endpoint:** `POST https://api.comfy.org/v2/models/luma/photon-flash-1`

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
            "luma/photon-flash-1",
            {
                "aspect_ratio": "1:1",
                "prompt": "a red circle on a plain white background",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    const { data } = await comfy.models.run("luma/photon-flash-1", {
      aspect_ratio: "1:1",
      prompt: "a red circle on a plain white background",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/luma/photon-flash-1 \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"aspect_ratio\": \"1:1\", \"prompt\": \"a red circle on a plain white background\"}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/luma/photon-flash-1/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y puedes recoger el resultado cuando esté listo, desde este proceso u otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) repasa el estado, la cancelación y la recopilación.

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
                "luma/photon-flash-1",
                {
                    "aspect_ratio": "1:1",
                    "prompt": "a red circle on a plain white background",
                },
            )
            print("request_id:", handle.request_id)  # junto con el ID del modelo, es todo lo que otro proceso necesita
    
            # Consulta una y otra vez hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
            async for update in handle.iter_events():
                print(update.status, update.queue_position)
    
            # La carga útil propia del proveedor, el mismo valor que devuelve models.run().
            # Una solicitud fallida o cancelada genera aquí el error tipado de Router.
            result = await handle.get()
    
        print(result)
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza para los reintentos automáticos.
    const handle = await comfy.models.submit("luma/photon-flash-1", {
      aspect_ratio: "1:1",
      prompt: "a red circle on a plain white background",
    });
    console.log("requestId:", handle.requestId); // junto con el ID del modelo, es todo lo que otro proceso necesita
    
    // Consulta una y otra vez hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud fallida o cancelada se rechaza aquí.
    const result = await handle.get();
    
    console.log(result.data);
    
    
    
    # 1. Enviar. Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/luma/photon-flash-1/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"aspect_ratio\": \"1:1\", \"prompt\": \"a red circle on a plain white background\"}"
    
    # 2. Consulta una y otra vez hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/luma/photon-flash-1/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recopilar. 200 con la salida nativa del modelo, 202 con el cuerpo de estado mientras aún se está ejecutando.
    curl https://api.comfy.org/v2/models/luma/photon-flash-1/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Esquema

### 

​

Entrada

​

aspect_ratio

string

predeterminado:"\"16:9\""

La relación de aspecto de la generaciónValores posibles: `1:1`, `16:9`, `9:16`, `4:3`, `3:4`, `21:9`, `9:21`

​

callback_url

string (uri)

La URL de callback para la generaciónFormato: `uri`

​

character_ref

object

​

character_ref.identity0

object

El objeto de identidad de imagen

​

character_ref.identity0.images

string (uri)[]

Las URL de la identidad de imagen

​

generation_type

string

predeterminado:"\"image\""

Valores posibles: `image`

​

image_ref

object[]

El objeto de referencia de imagen

​

image_ref[].url

string (uri)

La URL de la referencia de imagenFormato: `uri`

​

image_ref[].weight

number

El peso de la referencia de imagen

​

model

string

El modelo de imagen usado para la generación. En la ruta del Comfy Router `POST /v2/models/luma/{model}` este campo se toma de la ruta y NO DEBES enviarlo; en la ruta v1 `POST /proxy/luma/generations/image` está restringido al enum LumaImageModel (`photon-1`, `photon-flash-1`), que la Rewrite hace cumplir al rechazar un modelo omitido o desconocido.

​

modify_image_ref

object

El objeto de referencia de imagen a modificar

​

modify_image_ref.url

string (uri)

La URL de la referencia de imagenFormato: `uri`

​

modify_image_ref.weight

number

El peso de la referencia de imagen a modificar

​

prompt

string

El prompt de la generación

​

style_ref

object[]

El objeto de referencia de imagen

​

style_ref[].url

string (uri)

La URL de la referencia de imagenFormato: `uri`

​

style_ref[].weight

number

El peso de la referencia de imagen

Generado a partir del esquema que Router sirve en `GET /v2/models/luma/photon-flash-1/openapi.json`, el mismo documento con el que valida una llamada antes de que la solicitud llegue al proveedor.

### 

​

Salida

​

assets

object

Los recursos de una generación de imágenes. `image` es el resultado; `video` y `progress_video` pertenecen a la operación VIDEO de Dream Machine, que comparte esta ruta de estado, y Luma los envía aquí como null explícitos.

​

assets.image

string (uri)

La URL de la imagen generada: la hoja que rellena una generación de `luma/photon-*`. Es null hasta que la generación alcanza `completed`.Formato: `uri`

​

assets.progress_video

string (uri)

Siempre es null en una generación de imágenes; es la vista previa en curso que Luma publica mientras se ejecuta una generación de VIDEO.Formato: `uri`

​

assets.video

string (uri)

Siempre es null en una generación de imágenes; en su lugar lo rellenan los modelos de video `luma/ray-*`.Formato: `uri`

​

created_at

string (date-time)

La fecha y hora en que se creó la generaciónFormato: `date-time`

​

failure_reason

string

El motivo del estado de la generación

​

generation_type

string

El tipo de la generación: siempre `image` en esta operaciónValores posibles: `image`

​

id

string (uuid)

El ID de la generaciónFormato: `uuid`

​

model

string

El modelo usado para la generación

​

request

object

La solicitud de generación de imágenes, devuelta dentro del documento terminal. Luma serializa cada campo de su modelo de solicitud y escribe un `null` explícito en cada uno que el llamador no definió, así que lee la presencia de un campo a partir de su VALOR y no de la clave.

​

request.aspect_ratio

string

predeterminado:"\"16:9\""

La relación de aspecto de la generaciónValores posibles: `1:1`, `16:9`, `9:16`, `4:3`, `3:4`, `21:9`, `9:21`

​

request.callback_url

string (uri)

La URL de callback para la generaciónFormato: `uri`

​

request.character_ref

object

​

request.character_ref.identity0

object

Una identidad de imagen tal como vuelve dentro del documento terminal. Misma forma que `LumaImageIdentity`, con sus miembros anulables por el motivo que indica `LumaImageRefEcho`.

​

request.character_ref.identity0.images

string (uri)[]

Las URL de la identidad de imagen

​

request.generation_type

string

Siempre `image` cuando está definido, como eco de la operación. Es null cuando el llamador no envió uno, por el motivo por el que existe todo este objeto de eco.

​

request.image_ref

object[]

Una referencia de imagen tal como vuelve dentro del documento terminal. Misma forma que `LumaImageRef`, con cada miembro anulable porque Luma devuelve como eco un `null` explícito en los que no se definieron, en lugar de omitirlos.

​

request.image_ref[].url

string (uri)

La URL de la referencia de imagenFormato: `uri`

​

request.image_ref[].weight

number

El peso de la referencia de imagen

​

request.model

string

predeterminado:"\"photon-1\""

El modelo de imagen usado para la generaciónValores posibles: `photon-1`, `photon-flash-1`

​

request.modify_image_ref

object

Una referencia de imagen a modificar tal como vuelve dentro del documento terminal. Misma forma que `LumaModifyImageRef`, con sus miembros anulables por el motivo que indica `LumaImageRefEcho`.

​

request.modify_image_ref.url

string (uri)

La URL de la referencia de imagenFormato: `uri`

​

request.modify_image_ref.weight

number

El peso de la referencia de imagen a modificar

​

request.prompt

string

El prompt de la generación

​

request.style_ref

object[]

Una referencia de imagen tal como vuelve dentro del documento terminal. Misma forma que `LumaImageRef`, con cada miembro anulable porque Luma devuelve como eco un `null` explícito en los que no se definieron, en lugar de omitirlos.

​

request.style_ref[].url

string (uri)

La URL de la referencia de imagenFormato: `uri`

​

request.style_ref[].weight

number

El peso de la referencia de imagen

​

state

string

El estado de la generaciónValores posibles: `queued`, `dreaming`, `completed`, `failed`

## 

​

Ejemplos

### 

​

Entrada
    
    
    {
      "aspect_ratio": "1:1",
      "prompt": "a red circle on a plain white background"
    }
    

### 

​

Salida
    
    
    {
      "assets": {
        "image": "https://example.invalid/luma/photon-flash-1/generated.png",
        "progress_video": null,
        "video": null
      },
      "created_at": "2027-01-01T00:00:00Z",
      "failure_reason": null,
      "generation_type": "image",
      "id": "a1c73f26-08d5-4e69-b7a2-3c4d5e6f7a80",
      "model": "photon-flash-1",
      "request": {
        "aspect_ratio": "1:1",
        "callback_url": null,
        "character_ref": null,
        "generation_type": "image",
        "image_ref": null,
        "model": "photon-flash-1",
        "modify_image_ref": null,
        "prompt": "a red circle on a plain white background",
        "style_ref": null
      },
      "state": "completed"
    }
    

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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/luma/photon-flash-1/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/luma/photon-flash-1/code)

[Photon 1](https://docs.comfy.org/es/development/comfy-router/models/luma/photon-1/code)[Ray 2](https://docs.comfy.org/es/development/comfy-router/models/luma/ray-2/code)
